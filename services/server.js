'use strict';

require('dotenv').config();
var express = require('express');
var app = express();
var port = process.env.PORT || 3000;
var bodyParser = require('body-parser');
var server = require('http').Server(app);
var mongoose = require('mongoose');
var passport = require('passport');
var session = require('express-session');
var io = require('socket.io')(server);
var amqp = require('amqplib/callback_api');
require('./io/socket')(io);

global.io = io;

var Promise = require('bluebird')
var amqplib = require('amqplib')
var retry = require('amqplib-retry')
var CONSUMER_QUEUE = 'status'
var FAILURE_QUEUE = 'status.failure'

Promise
  .resolve(amqplib.connect('amqp://admin:password@' + process.env.AMQP_HOST))
  .then(function (conn) {
    return conn.createChannel()
  })
  .tap(function (channel) {
    return Promise.all([
      channel.assertQueue(CONSUMER_QUEUE, { durable: false, autoDelete: false }),
      channel.assertQueue(FAILURE_QUEUE, { durable: false, autoDelete: false })
    ])
  })
  .tap(function (channel) {
    console.log("AMQP Connected.")
    var messageHandler = function (msg) {
      // no need to 'ack' or 'nack' messages
      // messages that generate an exception (or a rejected Promise) will be retried
      console.log(msg.content.toString());
      io.emit('message', msg.content.toString());
    }

    channel.consume(CONSUMER_QUEUE, retry({
      channel: channel,
      consumerQueue: CONSUMER_QUEUE,
      failureQueue: FAILURE_QUEUE,
      handler: messageHandler
      //  delay: function (attempts) { return 1000; /* milliseconds */ }
    }))
  })

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/fbt');

var sessionOptions = {
  // key: 'session.sid',
  secret: 'Some secret key',
  resave: true,
  saveUninitialized: true,
  cookie: {
    // secure: true,
    maxAge: 600000,
    expires: false
  }
};

app.use(session(sessionOptions));
app.use(passport.initialize());
app.use(passport.session());

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

require('./routes/fbt_routes.js')(app);

server.listen(port);
