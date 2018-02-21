import requests, json, time, os
from requests.auth import HTTPBasicAuth

SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

GIT_LOG_SINCE = os.environ['GIT_LOG_SINCE']

CATALINA_PATH = '/pentaho/pentaho-server/tomcat/logs/catalina.out'
GITLOG_PATH = '/git-storage/gitlog.md'

#SERVER_STARTUP_TIME = 0 # 5 minutes
SERVER_STARTUP_TIME = 180 # 4 minutes
#SERVER_STARTUP_TIME = 10
VERSION_PREFIX = os.environ['RELEASE_VERSION']

with open('/pentaho/pentaho-server/pentaho-solutions/system/karaf/etc/startup.properties', 'r') as verf:
  ver = verf.read()
  i = ver.find(VERSION_PREFIX)
  VERSION = ver[i:ver.find("=",i)]
  print "the version found in the files: " + VERSION


# wait for server startup
time.sleep(SERVER_STARTUP_TIME)

with open(CATALINA_PATH, 'r') as logf:
  log = logf.read()

with open(GITLOG_PATH, 'r') as gitlogf:
  gitlog = gitlogf.read()

hasExceptions = log.lower().find("exception") >= 0
didStart = log.lower().find("server is ready") >= 0
testsPassed = True
errors = ""

if didStart:
  auth=HTTPBasicAuth('admin', 'password')
  h = {'Accept': 'application/json, text/javascript, */*; q=0.01'}

  session = requests.session()

  try:
    r = session.get('http://localhost:8080/pentaho/Home', auth=auth)
    if r.status_code == 200:
      print "Login successful"

      r = session.get('http://localhost:8080/pentaho/api/repo/files/%3A/tree?depth=-1&showHidden=false&filter=*%7CFOLDERS&_=1507833128478', headers=h)
      if r.status_code == 200:
        print "Repository tree fetched successfully"
        if r.text.find('/home/admin') >= 0 and r.text.find('/home/suzy') >= 0 and r.text.find('/public/Steel Wheels/') >= 0:
          print "Found required folders"

          # run a prpt
          r = session.post('http://localhost:8080/pentaho/plugin/reporting/api/jobs/reserveId')
          if r.status_code == 200:
            j = json.loads(r.text)

            data = {'line':'Classic Cars', 'output-target':'pageable/pdf', 'renderMode':'REPORT', 'reservedId': j['reservedId']}
            r = session.post('http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3AInventory%20List%20(report).prpt/reportjob', data=data)
            time.sleep(5)
            r = session.post('http://localhost:8080/pentaho/plugin/reporting/api/jobs/' + j['reservedId'] + '/content')

            if r.status_code == 200:
              print "Report generated successfully"
            else:
              print "Report generation failed"
              errors += ":x: Report generation failed :x: \n"
              testsPassed = False

            r = session.get('http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3AProduct%20Line%20Share%20by%20Territory.xanalyzer/editor')
            if r.status_code == 200:
              print "Analyzer successfully loaded"
            else:
              print "Analyzer failed to load"
              errors += ":x: Analyzer failed to load :x: \n"
              testsPassed = False

            r = session.get('http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ARegional%20Product%20Mix%20(dashboard).xdash/viewer')
            if r.status_code == 200:
              print "Dashboard successfully loaded"
            else:
              print "Dashboard failed to load"
              errors += ":x: Dashboard failed to load :x: \n"
              testsPassed = False

            r = session.get('http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3AVendor%20Sales%20Report%20(interactive%20report).prpti/prpti.view')
            if r.status_code == 200:
              print "Interactive Report loaded successfully"
            else:
              print "Interactive Report failed to load"
              errors += ":x: Interactive Report failed to load :x: \n"
              testsPassed = False
          else:
            print "Failed to reserve id for report"
            errors += ":x: Failed to reserve id for report :x: \n"
            testsPassed = False
        else:
          print "Required folders missing in repository"
          errors += ":x: Required folders missing in repository :x: \n"
          testsPassed = False
      else:
        errors += ":x: Repository tree fetch failed :x: \n"
        testsPassed = False
        print "Repository tree fetch failed"

    else:
      errors += ":x: Login failed, status_code = " + str(r.status_code) + ":x: \n"
      testsPassed = False
      print "Login failed, status_code = " + str(r.status_code)

  except requests.exceptions.RequestException as e:
    print "Server not responding..."
    errors += ":x: Could not login or server not responding :x: \n"
    testsPassed = False


# didStart
# hasExceptions
# testsPassed
status_message = ""
if didStart:
  if hasExceptions:
    status_message = ":warning: pentaho-server-" + VERSION + " started with *exceptions* :warning: \n"
#  else:
#    status_message = ":white_check_mark: pentaho-server-" + VERSION + " started successfully :white_check_mark: \n"

  if testsPassed:
    status_message += ":white_check_mark: pentaho-server-" + VERSION + " *passed* smoke-test validations :white_check_mark: \n"
  else:
    status_message += ":x: pentaho-server-" + VERSION + " *failed* smoke-test validations :x: \n"
    status_message += errors
else:
  status_message = ":x: pentaho-server-" + VERSION + " *failed* to start :x: \n"



print "Posting results to slack..."
session = requests.session()
data = {
         'token':SLACK_TOKEN,
         'channel':SLACK_CHANNEL,
         'text':status_message
       }

r = session.post('https://slack.com/api/chat.postMessage', data=data)

if didStart == False or testsPassed == False or hasExceptions:
  print "Posting snippet to slack since smoke test failed or exceptions present..."
  session = requests.session()
  data = {
           'token':SLACK_TOKEN,
           'channels':SLACK_CHANNEL,
           'content':log,
           'filename':'catalina.out',
           'filetype':'text'
#           'initial_comment':'this is it',
#           'title':'catalina.out_t'
         }
  r = session.post('https://slack.com/api/files.upload', data=data)

#print "Posting snippet to slack since smoke test failed or exceptions present..."
#session = requests.session()
#data = {
##         'token':SLACK_TOKEN,
#         'channels':SLACK_CHANNEL,
#         'file':gitlog,
#         'filename':'gitlog.html',
#         'filetype':'html'
#          'initial_comment':'this is it',
#          'title':'catalina.out_t'
#       }
#payload={
#  "filename":"gitlog.html",
#  "token":SLACK_TOKEN,
#  "channels":SLACK_CHANNEL
#}

#my_file = {
#  'file' : (GITLOG_PATH, open(GITLOG_PATH, 'rb'), 'html')
#}

#r = session.post('https://slack.com/api/files.upload', params=payload, files=my_file)

  session = requests.session()
  data = {
           'token':SLACK_TOKEN,
           'channel':SLACK_CHANNEL,
           'text':"*Recent GitHub activity (" + GIT_LOG_SINCE + "):*\n\n" + gitlog
         }
  r = session.post('https://slack.com/api/chat.postMessage', data=data)


