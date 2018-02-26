#!/bin/sh
service rabbitmq-server start
sleep 5
rabbitmqctl add_user admin password
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
FLASK_APP=/pentaho/commands.py flask run --host=0.0.0.0 &
