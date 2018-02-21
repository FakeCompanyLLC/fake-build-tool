#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

# build/start nexus3
#cd docker-nexus3
#echo "Building sonatype/nexus3"
#docker build -t sonatype/nexus3 .
#echo "Starting sonatype/nexus3..."
#docker run -d -p 8081:8081 --name nexus sonatype/nexus3
#cd ..

# build/start nexus
#cd docker-nexus
#echo "Building sonatype:nexus2"
#docker build -t sonatype:nexus2 oss
#echo "Starting sonatype:nexus2..."
#docker run -d -p 8081:8081 --name nexus sonatype:nexus2
#sleep 30
#cd ..

#cd web-res
#python -m SimpleHTTPServer 8000&
#HTTP_PID=$!
#cd ..

# build the pentaho stuff
cd docker-pentaho
echo "Building [pentaho-build] docker image..."
#docker build -t pentaho-build:7.1-SNAPSHOT . > /dev/null 2>&1
#docker build --no-cache -t pentaho-build:7.1-SNAPSHOT .
docker build -t pentaho-build:8.1.0.0-SNAPSHOT .

cd ..
#echo "Starting container... be sure env.list is setup"; sleep 3
#docker run -it --dns=10.100.2.155 --env-file=env.list --rm -v `pwd`/git-storage:/pentaho/git-storage -v `pwd`/root-storage:/root pentaho-build:8.1.0.0-SNAPSHOT
docker run -it --env-file=env.list --rm -v `pwd`/git-storage:/pentaho/git-storage -v `pwd`/root-storage:/root pentaho-build:8.1.0.0-SNAPSHOT
EXIT_STATUS=$?

# shutdown nexus
#docker stop nexus
#docker rm nexus
#kill $HTTP_PID

if [[ $EXIT_STATUS -eq 1 ]]; then
   echo "Build Failed - Halting";
   exit $EXIT_STATUS
fi

if [[ $EXIT_STATUS -eq 2 ]]; then
   # EXIT_STATUS == 2 means only git history
   exit 0
fi

if [[ $EXIT_STATUS -eq 3 ]]; then
   # EXIT_STATUS == 3 means no changes to build or test
   exit 0
fi

cd docker-smoker/docker
echo "Building [smoker] docker image..."
#docker build -t pentaho-build:7.1-SNAPSHOT . > /dev/null 2>&1
#docker build --no-cache -t pentaho-build:7.1-SNAPSHOT .
docker build -t snapshot_smoker .

cd ../..
#docker run -it --dns=10.100.2.155 --env-file=env.list --rm -v `pwd`/git-storage:/git-storage -v `pwd`/root-storage:/root snapshot_smoker
docker run -it --env-file=env.list --rm -p 8080:8080 -v `pwd`/git-storage:/git-storage -v `pwd`/root-storage:/root snapshot_smoker

