from subprocess import Popen, PIPE
import json, os, signal, psutil, time
from flask import Flask, request
from pprint import pprint
app = Flask(__name__)

build_process = None

@app.route("/build/run", methods=['POST'])
def run():
    contents = json.dumps(request.get_json())
    filename = '/pentaho/configuration/projects.json.' + str(time.time())
    f = open(filename, 'w')
    f.write(contents)
    f.close()
    build_process = Popen('/pentaho/build-all.sh ' + filename, shell=True, stdin=PIPE, stdout=PIPE)
    return json.dumps({'command':'run'})

@app.route("/build/stop")
def stop():
    global build_process
    if build_process and build_process.pid:
        try:
          parent = psutil.Process(build_process.pid)
        except psutil.NoSuchProcess:
          return
        children = parent.children(recursive=True)
        for process in children:
          process.send_signal(signal.SIGTERM)

    build_process = None
    return json.dumps({'command':'stop'})
