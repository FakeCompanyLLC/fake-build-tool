#!/bin/sh

nginx
service mongod start
cd /app/services
node server.js &
mongod &
