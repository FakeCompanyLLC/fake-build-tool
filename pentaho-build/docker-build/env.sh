#!/bin/bash

#export PHANTOM_HOME=/pentaho/phantomjs-2.1.1-linux-x86_64

export ANT_HOME=/pentaho/apache-ant-1.10.1
export MAVEN_HOME=/pentaho/apache-maven-3.3.9
export RJS_PATH=`which r.js`

#export PATH=$ANT_HOME/bin:$MAVEN_HOME/bin:$PHANTOM_HOME/bin:$PATH
export PATH=$ANT_HOME/bin:$MAVEN_HOME/bin:$PATH

export DEFAULT_BRANCH=master
export MAVEN_OPTS=-Dpentaho.resolve.repo=http://172.17.0.1:8081/nexus/content/groups/public

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
