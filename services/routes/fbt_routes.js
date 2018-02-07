'use strict';

module.exports = function(app) {
  var fbt = require('../controllers/fbt_controller');

  var root = '/api/fbt';

  app.route(root + '/projects')
    .get(fbt.read_projects)

  app.route(root + '/project')
    .post(fbt.create_project)

  app.route(root + '/project/:id')
    .get(fbt.read_project)
    .put(fbt.update_project)

  app.route(root + '/project/:id/instance')
    .post(fbt.create_project_instance)

  app.route(root + '/project/instance/:id')
    .put(fbt.update_project_instance)

  app.route(root + '/profile')
    .post(fbt.create_profile)

  app.route(root + '/profile/:id')
    .get(fbt.read_profile)
    .put(fbt.update_profile)

  app.route(root + '/profiles')
    .get(fbt.profiles)

  app.route(root + '/profile/:id/copy')
    .post(fbt.copy_profile)
}
