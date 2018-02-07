'use strict';

module.exports = function(io) {
  io.on('connect', function(socket) {
    console.log(socket.id + " connected.");
  });
}
