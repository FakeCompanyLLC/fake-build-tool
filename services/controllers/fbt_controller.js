var mongoose = require('mongoose')
require('../models/fbt_model.js')
var Profile = mongoose.model('Profile')
var Project = mongoose.model('Project')
var ProjectName = mongoose.model('ProjectName')
var ProjectInstance = mongoose.model('ProjectInstance')
var ProjectInstanceMapping = mongoose.model('ProjectInstanceMapping')

var fs = require("fs");
var contents = fs.readFileSync("projects.json");

function save(projectJson) {
  var projectName = new ProjectName();
  projectName._id = new mongoose.Types.ObjectId();
  projectName.name = projectJson['name'];
  delete projectJson['name'];

  var projectInstance = new ProjectInstance(projectJson);
  projectInstance._id = new mongoose.Types.ObjectId();
  projectInstance.name = "Default";

  return new Promise(function(resolve, reject) {
    var project = new Project();
    project._id = new mongoose.Types.ObjectId();
    projectName.save((err, projectName) => {
      project.name = projectName;
      projectInstance.save((err, projectInstance) => {
        project.instances = [projectInstance];
        project.save((err, project) => {
          console.log("Saved " + projectName.name);
          setTimeout(function() {
            resolve();
          }, 100);
        });
      });
    });
  });
}

async function load(contents) {
  var jsonContent = JSON.parse(contents);
  for (var i = 0; i < jsonContent.length; i++) {
    let projectJson = jsonContent[i];
    await save(projectJson);
  }
}
// load(contents);

exports.read_projects = function(req, res) {
  Project.find({}, function(err, projects) {
    if (err) res.send(err);
    res.json(projects);
  }).populate('name').populate('instances');
}

exports.create_project = function(req, res) {
  var project = new Project();
  project._id = new mongoose.Types.ObjectId();
  var projectName = new ProjectName(req.body);
  projectName._id = new mongoose.Types.ObjectId();
  var projectInstance = new ProjectInstance();
  projectInstance._id = new mongoose.Types.ObjectId();
  projectInstance.name = "Default";
  projectInstance.save((err, projectInstance) => {
    projectName.save((err, projectName) => {
      project.name = projectName;
      project.instances = [projectInstance];
      project.save(function(err) {
        if (err) res.send(err);
        res.json(project);
      });
    });
  });
}

exports.create_project_instance = function(req, res) {
  Project.findById(req.params.id, (err, project) => {
    var projectInstance = new ProjectInstance(req.body);
    projectInstance._id = new mongoose.Types.ObjectId();
    projectInstance.save((err, projectInstanceSaved) => {
      project.instances.push(projectInstanceSaved._id);
      project.save((err, project) => {
        res.json(projectInstance);
      });
    });
  });
}

exports.update_project_instance = function(req, res) {
  ProjectInstance.findByIdAndUpdate(req.params.id, req.body, function(err, projectInstance) {
    if (err) res.send(err);
    res.json(projectInstance);
  });
}

exports.read_project = function(req, res) {
  Project.findById(req.params.id, function(err, project) {
    if (err) res.send(err);
    res.json(project);
  }).populate('name').populate('instances');
}

exports.update_project = function(req, res) {
  Project.findById(req.params.id, function (err, project) {
    console.log(project);
    console.log(req.body.instance);
    if (err) res.send(err);
    ProjectName.findByIdAndUpdate(project.name._id, req.body.name, (err, projectName) => {
      ProjectInstance.findByIdAndUpdate(project.instance._id, req.body.instance, (err, projectInstance) => {
        res.json(project);
      });
    })
  }).populate('name instance');
}

exports.create_profile = function(req, res) {
  var profile = new Profile(req.body);
  profile._id = new mongoose.Types.ObjectId();
  profile.save(function(err) {
    if (err) res.send(err);
    res.json(profile);
  });
}

exports.read_profile = function(req, res) {
  Profile.findById(req.params.id, function(err, profile) {
    if (err) res.send(err);
    res.json(profile);
  }).populate({
    path: 'projects',
    populate: [{
      path: 'project',
      populate: [{
        path: 'name'
      }, {
        path: 'instances'
      }]
    }, {
      path: 'instance'
    }]
  });
}

exports.update_profile = function(req, res) {
  Profile.findById(req.params.id, function(err, profile) {
    if (err) res.send(err);
    var m = [];
    var promises = [];
    req.body.projects.forEach(mapping => {
      promises.push(new Promise((resolve, reject) => {
        var projectInstanceMapping = new ProjectInstanceMapping();
        projectInstanceMapping._id = new mongoose.Types.ObjectId();
        projectInstanceMapping.project = mapping.project._id;
        projectInstanceMapping.instance = mapping.instance._id;
        projectInstanceMapping.save((err, map) => {
          m.push(map);
          resolve();
        });
      }));
    });
    console.log(promises.length);
    Promise.all(promises).then(function() {
      profile.projects = m;
      profile.save((err, profile) => {
        res.json(profile);
      });
    });
  });
}

exports.profiles = function(req, res) {
  Profile.find({}, function(err, profiles) {
    if (err) res.send(err);
    res.json(profiles);
  }).select('name _id')
}

exports.copy_profile = function(req, res) {
  Profile.findById(req.params.id, function(err, profile) {
    if (err) res.send(err);
    console.log(profile);
    var promises = [];
    profile.projects.forEach(project => {
      var promise = new Promise((resolve, reject) => {
        project._id = new mongoose.Types.ObjectId();
        project.isNew = true;
        project.save((err, project) => {
          resolve(project._id);
        });
      });
      promises.push(promise);
    });
    Promise.all(promises).then(values => {
      profile.name = profile.name + " copy";
      profile._id = new mongoose.Types.ObjectId();
      profile.isNew = true;
      profile.projects = values;
      profile.save((err, profile) => {
        res.json(profile);
      });
    });
  }).populate('projects');
}
