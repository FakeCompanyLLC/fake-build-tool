#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

cd pentaho-build/docker-pentaho
echo "Building [pentaho-build] docker image..."
docker build -t pentaho-build:8.1.0.0-SNAPSHOT .

cd ../..

docker build -t fbt-build:8.1.0.0-SNAPSHOT .

docker network create fbt-net
docker stop fbt-server
docker rm fbt-server
docker run --name fbt-server --net fbt-net -P -p 5000:5000 -p 5672:5672 -it -d --dns=10.100.2.155 --env-file=pentaho-build/env.list --rm -v `pwd`/configuration:/pentaho/configuration -v `pwd`/pentaho-build/git-storage:/pentaho/git-storage -v `pwd`/pentaho-build/root-storage:/root fbt-build:8.1.0.0-SNAPSHOT
# EXIT_STATUS=$?
#
# if [[ $EXIT_STATUS -eq 1 ]]; then
#    echo "Build Failed - Halting";
#    exit $EXIT_STATUS
# fi
#
# if [[ $EXIT_STATUS -eq 2 ]]; then
#    # EXIT_STATUS == 2 means only git history
#    exit 0
# fi
#
# if [[ $EXIT_STATUS -eq 3 ]]; then
#    # EXIT_STATUS == 3 means no changes to build or test
#    exit 0
# fi
