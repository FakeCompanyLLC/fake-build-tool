'use strict';

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ProjectInstanceSchema = new Schema({
  _id: Schema.Types.ObjectId,
  name: String,
  "version-override": String,
  remotes: Array,
  tag: String,
  commit: String,
  "revert-commit": String,
  "cherry-picks": Array,
  modules: Array,
  cmd: Array,
  properties: Array,
  profile: String,
  auth: Boolean,
  "replace-subfloor": Boolean,
  branch: String,
  "copy-overrides": Boolean,
  fork: String,
  deploy: Boolean
});

var ProjectNameSchema = new Schema({
  _id: Schema.Types.ObjectId,
  name: String
});

var ProjectSchema = new Schema({
  _id: Schema.Types.ObjectId,
  name: {type: Schema.Types.ObjectId, ref: 'ProjectName'},
  instances: [{type: Schema.Types.ObjectId, ref: 'ProjectInstance'}]
});

var ProjectInstanceMappingSchema = new Schema({
  _id: Schema.Types.ObjectId,
  project: {type: Schema.Types.ObjectId, ref: 'Project'},
  instance: {type: Schema.Types.ObjectId, ref: 'ProjectInstance'},
  order: Number
});

var ProfileSchema = new Schema({
  _id: Schema.Types.ObjectId,
  name: String,
  status: String,
  lastRun: Date,
  projects: [{type: Schema.Types.ObjectId, ref:'ProjectInstanceMapping'}]
});

module.exports = mongoose.model('Profile', ProfileSchema);
module.exports = mongoose.model('Project', ProjectSchema);
module.exports = mongoose.model('ProjectName', ProjectNameSchema);
module.exports = mongoose.model('ProjectInstance', ProjectInstanceSchema);
module.exports = mongoose.model('ProjectInstanceMapping', ProjectInstanceMappingSchema);
