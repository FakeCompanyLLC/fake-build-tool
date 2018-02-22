from projects import projects
import os, shlex, shutil, time, sys, json, requests, gitjson, slack, buildlib

reload(sys)
sys.setdefaultencoding('utf8')

os.chdir("/pentaho/git-storage")
cwd = os.getcwd() + "/"

BUILDLOG_PATH = cwd + 'build.log'
buildlog = open(BUILDLOG_PATH, "w")

GIT_HISTORY_ONLY = 'True' == os.environ['GIT_HISTORY_ONLY']

# get last build date
LASTBUILDDATEPATH = cwd + 'lastbuilddate.txt'
LAST_BUILD_DATE = 0
try:
  with open(LASTBUILDDATEPATH, 'r') as lastbuilddatef:
     LAST_BUILD_DATE = int(lastbuilddatef.read())
except:
  LAST_BUILD_DATE = 0

print "\nUpdating git projects..."
# update git repositories
buildlib.updateGit(cwd, buildlog, projects)
buildlib.update_progress(time.time() - buildlib.start_time, 1, str(len(projects)) + "/" + str(len(projects)) + " [Complete]\n")

# gather git history
print "\nGathering git history..."
commits1y = buildlib.getHistory(cwd, projects, "1 year ago")
commits180d = buildlib.getHistory(cwd, projects, "180 days ago")
commits90d = buildlib.getHistory(cwd, projects, "90 days ago")
commits30d = buildlib.getHistory(cwd, projects, "30 days ago")
commits7d = buildlib.getHistory(cwd, projects, "7 days ago")
commits3d = buildlib.getHistory(cwd, projects, "3 days ago")
commits1d = buildlib.getHistory(cwd, projects, "1 day ago")

print "\nGenerating history reports..."
buildlib.writeLog(cwd, commits1y, "1 year ago", "1y")
buildlib.writeLog(cwd, commits180d, "180 days ago", "180d")
buildlib.writeLog(cwd, commits90d, "90 days ago", "90d")
buildlib.writeLog(cwd, commits30d, "30 days ago", "30d")
buildlib.writeLog(cwd, commits7d, "7 days ago", "7d")
buildlib.writeLog(cwd, commits3d, "3 days ago", "3d")
buildlib.writeLog(cwd, commits1d, "1 day ago", "1d")


# check if changes to ivy.xml or pom.xml exist
print "\nAnalyzing commit history for possible dependency changes..."
dependencyChanges = buildlib.getPossibleDependencyChanges(commits7d, LAST_BUILD_DATE)
if dependencyChanges != "":
  print dependencyChanges
  dependencyChanges = "*Possible dependency changes detected*\n\n" + dependencyChanges
  # notify buildteam of possibly dependency changes
  #slack.postMessage(slack.SLACK_TOKEN, slack.SLACK_CHANNEL, dependencyChanges)

if GIT_HISTORY_ONLY:
  print "\nHistory generated successful, exiting."
  exit(2)

# determine earliest changed dependency
indexOfHighestDependencySinceLastBuild = 0
if LAST_BUILD_DATE != 0:
  indexOfHighestDependencySinceLastBuild = len(projects)
  for c in commits7d:
    if int(c['date']) > LAST_BUILD_DATE:
      if c['index'] < indexOfHighestDependencySinceLastBuild:
        indexOfHighestDependencySinceLastBuild = c['index']

if indexOfHighestDependencySinceLastBuild == len(projects):
  print "\nNo changes since last build, exiting."
  exit(3)

#indexOfHighestDependencySinceLastBuild = 114

print "Start rebuilding from: " + str(projects[indexOfHighestDependencySinceLastBuild]['name'])
LAST_BUILD_DATE = int(round(time.time() * 1000))

buildlib.buildProjects(projects, indexOfHighestDependencySinceLastBuild, cwd, buildlog)

# update last build date/time
with open(LASTBUILDDATEPATH, 'w') as lastbuilddatef:
   lastbuilddatef.write(str(LAST_BUILD_DATE)[:-3])

buildlib.update_progress(time.time() - buildlib.start_time, len(projects)/float(len(projects)), str(len(projects)) + "/" + str(len(projects)) )
print ""
print "Build successful."
