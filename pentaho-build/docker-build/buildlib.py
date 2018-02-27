from subprocess import call, Popen, PIPE
from operator import itemgetter
import os, shlex, shutil, time, sys, json, requests
import gitjson, slack

start_time = time.time()
USER = os.environ['GIT_USER']
PASS = os.environ['GIT_PASS']
GIT_LOG_SINCE = os.environ['GIT_LOG_SINCE']
DEFAULT_FORK = os.environ['DEFAULT_FORK']

def update_progress(sec_elapsed, progress, statusText):
    barLength = 10 # Modify this to change the length of the progress bar
    block = int(round(barLength*progress))
    text = "\r{0} [{1}] {2: =3d}%".format( hms_string(sec_elapsed), "#"*block + "-"*(barLength-block), int(progress*100)) + " " + statusText
    print '\x1b[2K\r',
    sys.stdout.write(text)
    sys.stdout.write("\r")
    sys.stdout.flush()

def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60.
    return "{:>02}:{:>02}:{:>02}".format(h, m, int(s))

def tail(f, n):
  stdin,stdout = os.popen2("tail -n "+str(n)+" "+f)
  stdin.close()
  lines = stdout.read(); stdout.close()
  return lines

def getHistory(cwd, projects, gitLogSince=GIT_LOG_SINCE):
  projIndex = 0
  gitloglist = []
  commits = []
  for p in projects:
    skipGitLog = ( p['name'] in gitloglist) == True
    if not skipGitLog:
      os.chdir(cwd + p['fork'] + "/" + p['name'])
      gitloglist.append( p['name'] )
      gitlogjson = gitjson.git_log(["log", "--no-merges", "--since", gitLogSince], '')

      for c in gitlogjson:
        c['project'] = p['name']
        c['projecturl'] = 'https://github.com/' + p['fork'] + '/' + p['name']
        c['commiturl'] = c['projecturl'] + '/commit/' + c['sha']
        c['fork'] = p['fork']
        c['index'] = projIndex

      commits.extend(gitlogjson)
    projIndex+=1

  commits = sorted(commits, key=itemgetter('date'), reverse=True)
  return commits


def updateGit(cwd, f, projects):
  projIndex = 0

  alreadyUpdatedList = []
  for p in projects:
    skipUpdate = ( p['name'] in alreadyUpdatedList) == True
    if not skipUpdate:
      alreadyUpdatedList.append( p['name'] )
      update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [init]")
      skipInit = 'skipInit' in p and p['skipInit']
      fork = DEFAULT_FORK
      if 'fork' in p:
        fork = p['fork']
      p['fork'] = fork

      BRANCH = 'master'
      if 'branch' in p:
        BRANCH = p['branch']

      if not skipInit:
        if not os.path.isdir(cwd + fork):
          os.mkdir(cwd + fork)
        os.chdir(cwd + fork)

        if not 'auth' in p and not 'url' in p:
          p['url'] = 'https://github.com/' + fork + '/' + p['name']
        elif 'auth' in p:
          p['url'] = 'https://' + USER + ":" + PASS + '@github.com/' + fork + '/' + p['name']

        if ('tag' in p or 'branch' in p or 'commit' in p) and not os.path.isdir(cwd + fork + "/" + p['name']):
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git clone]")
          call( ["git", "clone", p['url']], stdout=f, stderr=f )
        elif not os.path.isdir(cwd + fork + "/" + p['name']):
          #for now skip shallow clones
          #update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git clone --depth=1]")
          #call( ["git", "clone", "--depth=1", p['url']], stdout=f, stderr=f )
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git clone]")
          call( ["git", "clone", p['url']], stdout=f, stderr=f )

        os.chdir(cwd + fork + "/" + p['name'])

        if 'remotes' in p:
          for remote in p['remotes']:
            if not 'auth' in p:
              remoteURL = 'https://github.com/' + remote + '/' + p['name']
            elif 'auth' in p:
              remoteURL = 'https://' + USER + ":" + PASS + '@github.com/' + remote + '/' + p['name']

            #print "adding " + remote + " ===> " + remoteURL
            call( ["git", "remote", "add", remote, remoteURL], stdout=f, stderr=f )
            call( ["git", "fetch", remote], stdout=f, stderr=f )

        if 'tag' in p or 'branch' in p or 'commit' in p or 'revert-commit' in p:
          call( ["git", "config", "remote.origin.fetch", "+refs/heads/*:refs/remotes/origin/*"], stdout=f, stderr=f )
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git fetch]")
          call( ["git", "fetch"], stdout=f, stderr=f )
        else:
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git fetch]")
          call( ["git", "fetch"], stdout=f, stderr=f )

        call( ["git", "stash"], stdout=f, stderr=f )
        call( ["git", "stash", "clear"], stdout=f, stderr=f )
        call( ["git", "reset", "--hard", "origin/" + BRANCH], stdout=f, stderr=f )

        if 'tag' in p:
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git checkout " + p['tag'] + "]")
          call( ["git", "checkout", p['tag']], stdout=f, stderr=f )
        elif 'branch' in p:
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git reset --hard origin/" + p['branch'] + "]")
          call( ["git", "reset", "--hard", "origin/" + p['branch']], stdout=f, stderr=f )
        elif 'commit' in p:
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git reset --hard " + p['commit'] + "]")
          call( ["git", "reset", "--hard", p["commit"] ], stdout=f, stderr=f )

        if 'revert-commit' in p:
          update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git revert -n " + p['revert-commit'] + "]")
          call( ["git", "revert", "-n", p['revert-commit'] ], stdout=f, stderr=f )

        if 'cherry-picks' in p:
          for pick in p['cherry-picks']:
            call( ["git", "cherry-pick", pick], stdout=f, stderr=f )

        if 'rebases' in p:
          for rebase in p['rebases']:
            call( ["git", "rebase", "--committer-date-is-author-date", rebase], stdout=f, stderr=f )

        update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + " [git clean -fd]")
        #call( ["git", "clean", "-fd"], stdout=f, stderr=f )

    projIndex+=1


def buildProjects(projects, startIndex, cwd, f, gitLogSince=GIT_LOG_SINCE, sinceExtension=""):
  GITLOG_PATH = cwd + 'gitlog' + sinceExtension + '.md'
  BUILDLOG_PATH = cwd + 'build.log'

  projIndex=startIndex
  print "\nBuilding projects..."
  for p in projects[projIndex:]:

    fork = DEFAULT_FORK
    if 'fork' in p:
      fork = p['fork']

    BRANCH = 'master'
    if 'branch' in p:
      BRANCH = p['branch']

    if not 'modules' in p:
      p['modules'] = [ '.' ]

    if 'module-override' in p:
      for moduleOverridePath in p['module-override']:
        shutil.copyfile("/pentaho/override.properties", os.getcwd() + "/" + moduleOverridePath + "/override.properties")

    for i, module in enumerate(p['modules']):

      os.chdir(cwd + fork + "/" + p['name'] + "/" + module)

      isMaven = os.path.exists(os.getcwd() + "/pom.xml")
      isDeploy = 'deploy' in p and p['deploy']
      hasProfile = 'profile' in p

      if not 'cmd' in p:
        if isMaven:
          cmdStr = 'mvn -DskipTests -Dpentaho.public.release.repo=http://172.17.0.1:8081/nexus/content/repositories/releases -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots clean'
          if isDeploy:
            cmdStr += " deploy"
          else:
            cmdStr += " install"
          if hasProfile:
            cmdStr += " -P " + p['profile']
          if 'properties' in p:
            for prop in p['properties']:
              cmdStr += " -D" + prop
          p['cmd'] = [ cmdStr ]
          #print "CMD: " + cmdStr
        else:
          cmdStr = 'ant -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots clean-all resolve dist'
          if isDeploy:
            cmdStr += " publish"
          else:
            cmdStr += " publish-local"
          p['cmd'] = [ cmdStr ]

      if module == '.':
        module = p['name']

      update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + ":" + module)

      if not 'copy-overrides' in p or p['copy-overrides']:
        shutil.copyfile("/pentaho/override.properties", os.getcwd() + "/override.properties")
      if 'replace-subfloor' in p and p['replace-subfloor']:
        #print "Replacing subfloor........."
        shutil.copyfile("/pentaho/subfloor.xml", os.getcwd() + "/build-res/subfloor.xml")
        shutil.copyfile("/pentaho/publish.xml", os.getcwd() + "/build-res/publish.xml")
        shutil.copyfile("/pentaho/ivysettings.xml", os.getcwd() + "/build-res/ivysettings.xml")

      if 'overrides' in p:
        for override in p['overrides']:
          o = open(os.getcwd() + "/override.properties", "a")
          o.write(override)
          o.close()

      if 'version-override' in p:
        o = open(os.getcwd() + "/override.properties", "a")
        o.write("project.revision=" + p['version-override'])
        o.close()

        if isMaven:
          for precmd in ['mvn versions:set -DnewVersion=' + p['version-override'], 'mvn versions:update-child-modules']:
            update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + ":" + module + " [" + precmd  + "]")
            cmd = shlex.split(precmd)
            call( cmd, stdout=f, stderr=f )

      for cmdStr in p['cmd']:
        update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + ":" + module + " [building]")
        cmd = shlex.split(cmdStr)
        retCode = call( cmd, stdout=f, stderr=f )
        update_progress(time.time() - start_time, projIndex/float(len(projects)), str(projIndex+1) + "/" + str(len(projects)) + " " + p['name'] + ":" + module + " [finished]")
        if retCode == 1:
          print ""
          print "Build failed, halting."
          f.close()
          # post build failed results to slack
          with open(GITLOG_PATH, 'r') as gitlogf:
            gitlogstr = gitlogf.read()

          text = "*BUILD FAILED* on project: " + p['name'] + "\n\n"
          slack.postMessage(slack.SLACK_TOKEN, slack.SLACK_CHANNEL, text)

          # read last 100 lines of build.log
          text = "*Tail of build.log*\n\n" + tail(BUILDLOG_PATH, 50)
          slack.postMessage(slack.SLACK_TOKEN, slack.SLACK_CHANNEL, text)

          text = "*Recent GitHub activity (" + gitLogSince + "):*\n\n" + gitlogstr
          slack.postMessage(slack.SLACK_TOKEN, slack.SLACK_CHANNEL, text)

          exit( retCode )
    projIndex+=1
    #os.chdir(cwd)


def writeLog(cwd, sortedCommits, gitLogSince=GIT_LOG_SINCE, sinceExtension=""):
  GITLOG_PATH = cwd + 'gitlog' + sinceExtension + '.md'
  GITLOGHTML_PATH = cwd + 'gitlog' + sinceExtension + '.html'

  gitlog = open(GITLOG_PATH, "w")
  gitloghtml = open(GITLOGHTML_PATH, "w")
  gitloghtml.write("<html><head><style>table { border-collapse: collapse; } table, th, td { border: 1px solid black; } .zr { white-space: nowrap; } .zre { white-space: nowrap; text-overflow:ellipsis; overflow: hidden; max-width:1px; }</style></head><body><table>")
  gitloghtml.write("<colgroup><col width=\"0%\"/><col width=\"0%\"/><col width=\"0%\"/><col width=\"0%\"/><col width=\"100%\"/></colgroup>")
  gitloghtml.flush()

  for c in sortedCommits:
    # html
    gitloghtml.write("<tr>")
    gitloghtml.write("<td class=zr><a href=\"" + c['projecturl'] + "\">" + c['project'] + "</a></td>")
    gitloghtml.write("<td class=zr><a href=\"" + c['commiturl'] + "\" target=\"_blank\">" + c['sha'] + "</a></td>")
    gitloghtml.write("<td class=zr>" + c['date_iso'] + "</td>")
    gitloghtml.write("<td class=zr><div title=\"" + c['email'].encode("utf8") + "\">" + c['name'].encode("utf8") + "</div></td>")
    gitloghtml.write("<td class=zre>" + c['subject'] + "</td>")
    gitloghtml.write("</tr>")

    # markdown
    gitlog.write("*" + c['date_iso'] + "*")
    gitlog.write(" *" + c['name'].encode("utf8") + "*")
    gitlog.write("\n*" + c['subject'] + "*")
    gitlog.write(" " + c['commiturl'])
    gitlog.write("\n\n")
  gitloghtml.write("</table></body></html>")
  gitloghtml.close()
  gitlog.close()


def getPossibleDependencyChanges(commits, LAST_BUILD_DATE):
  dependencyChanges = ""
  for c in commits:
    for fc in c['files']:
      if fc['path'].endswith("pom.xml") or fc['path'].endswith("ivy.xml"):
        if int(c['date']) > LAST_BUILD_DATE:
          dependencyChanges += c['project'] + "/" + fc['path'] + " has changed from commit " + c['commiturl'] + "\n"
  return dependencyChanges

