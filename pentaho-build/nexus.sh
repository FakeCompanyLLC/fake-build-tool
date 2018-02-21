#!/bin/bash

# build/start nexus3
#cd docker-nexus3
#echo "Building sonatype/nexus3"
#docker build -t sonatype/nexus3 .
#echo "Starting sonatype/nexus3..."
#docker run -d -p 8081:8081 --name nexus sonatype/nexus3
#cd ..

# build/start nexus
cd docker-nexus
echo "Building sonatype:nexus2"
docker build -t sonatype:nexus2 oss
echo "Starting sonatype:nexus2..."
cd ..
docker run -d -p 8081:8081 --name nexus -v `pwd`/nexus-storage:/sonatype-work sonatype:nexus2
