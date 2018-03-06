#
# { 'name': 'git-repository-name',
#   'fork': 'pentaho', #specify if not default
#   'branch': 'feature-branch', #specify a branch to build
#   'auth': True, #specify if github auth required
#   'remotes': [ 'mdamour1976', 'someone' ], #add additional remotes
#   'cherry-picks': [ 'commit-sha1', 'commit-sha2' ], #cherry-picks to apply
#   'reverts': [ 'commit-sha1', 'commit-sha2' ], #commits to revert
#   'profile': 'maven-profile', #maven profile to build
#   'modules': [ 'module-path1', 'module-path2' ], #maven modules to build
#   'properties': [ 'property1', property2' ], #maven properties to set
#   'cmd': [ 'any command you want', 'cmd2' ] # execute arbitrary commands in project
# }

projects = [

  { 'name': 'maven-parent-poms' },

  { 'name': 'pentaho-application-launcher' },

  { 'name': 'pentaho-commons-gwt-modules' },

  { 'name': 'pentaho-commons-xul' },

  { 'name': 'apache-vfs-browser' },

  { 'name': 'pentaho-commons-json' },

  { 'name': 'pentaho-kettle',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'pentaho-commons-database',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'pentaho-commons-database',
    'modules': ['model'] },

  { 'name': 'pentaho-connections' },

  { 'name': 'pentaho-actionsequence-dom' },

  { 'name': 'pentaho-versionchecker' },

  { 'name': 'pentaho-platform',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'mondrian',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'pentaho-reporting',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'metastore' },

  { 'name': 'pentaho-reporting',
    'modules': [ 'libraries' ],
    'properties': [ 'libraries' ] },

  { 'name': 'pentaho-registry' },

  { 'name': 'pentaho-osgi-bundles',
    'properties': [ 'skipDefault' ],
    'profile': 'lowdeps' },

  { 'name': 'mondrian',
    'modules': ['mondrian'] },

  { 'name': 'pentaho-platform',
    'properties': [ 'skipDefault' ],
    'modules': [ 'api' ] },

  { 'name': 'pentaho-reporting',
    'modules': [ 'engine' ],
    'properties': [ 'libraries' ] },

  { 'name': 'pentaho-kettle',
    'properties': [ 'skipDefault' ],
    'profile': 'base' },

  { 'name': 'pentaho-metadata' },

  { 'name': 'pentaho-kettle',
    'properties': [ 'skipDefault' ],
    'profile': 'plugins,lowdeps' },

  { 'name': 'pentaho-chartbeans' },

  { 'name': 'pdi-dataservice-plugin' },

  { 'name': 'pentaho-reportwizard-core' },

  { 'name': 'pentaho-reporting',
    'modules': [ 'engine' ],
    'properties': [ 'engine' ] },

  { 'name': 'pentaho-platform',
    'properties': [ 'skipDefault' ],
    'profile' : 'platform-base' },

  { 'name': 'pentaho-concurrent',
    'auth': True,
    'version-override': '1.0.0',
    'cmd': [ 'mvn clean install -Dpentaho.public.release.repo=http://172.17.0.1:8081/nexus/content/repositories/releases' ] },

  { 'name': 'pentaho-cwm',
#    'tag': '1.5.4',
    'branch': '1.5',
    'copy-overrides': True,
    'version-override': '1.5.4',
    'replace-subfloor': True,
    'cmd': [ 'ant -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots clean-all resolve dist publish-local' ] },
#-Dpentaho.resolve.repo=http://172.17.0.1:8081/content/groups/omni -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots clean-all resolve dist publish-local' ] },
#10.177.175.248

  { 'name': 'pentaho-simple-jndi' },

  { 'name': 'pentaho-simple-jndi',
    'version-override': '1.0.0',
    'cmd': [ 'mvn clean install -Dpentaho.public.release.repo=http://172.17.0.1:8081/nexus/content/repositories/releases' ] },

  { 'name': 'pdi-palo-core' },

  { 'name': 'pentaho-mongo-utils' },

  { 'name': 'pentaho-mongodb-plugin' },

  { 'name': 'pentaho-metaverse' },

  { 'name': 'pentaho-commons-database',
    'modules': ['gwt'] },

  { 'name': 'modeler' },

  { 'name': 'cpf',
    'fork': 'webdetails' },

  { 'name': 'ccc',
    'fork': 'webdetails' },

  { 'name': 'cdf',
    'fork': 'webdetails',
    'cmd': [ 'mvn clean install -DskipTests -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/snapshots/releases' ] },

  { 'name': 'pentaho-platform-plugin-common-ui' },

  { 'name': 'pentaho-platform-plugin-reporting' },

  { 'name': 'pdi-osgi-bridge',
    'branch': 'master' },

  { 'name': 'pentaho-osgi-bundles',
    'profile': 'highdeps' },

  { 'name': 'pentaho-kettle',
    'modules': [ 'plugins' ],
    'profile': 'highdeps' },

  { 'name': 'data-access' },

  { 'name': 'cda',
    'fork': 'webdetails' },

  { 'name': 'cde',
    'deploy': True,
    'fork': 'webdetails' },

  { 'name': 'pdi-platform-plugin' },

  { 'name': 'pentaho-platform-plugin-jpivot' },

  { 'name': 'pentaho-hdfs-vfs' },

  { 'name': 'pentaho-s3-vfs' },

  { 'name': 'oss-licenses',
    'auth': True },

  { 'name': 'pentaho-hadoop-shims',
    'profile': 'api,shims,all',
    'properties': [ 'skipDefault' ] },

  { 'name': 'marketplace' },

  { 'name': 'pdi-dataservice-server-plugin' },

  { 'name': 'pentaho-data-refinery' },

  { 'name': 'big-data-plugin',
    'cmd': ['mvn --non-recursive clean install -DskipTests'] },

  { 'name': 'big-data-plugin',
    'properties': [ 'featuresOnly' ] },

  { 'name': 'pentaho-ee',
    'remotes': [ 'mdamour1976' ],
    'modules': [ 'adaptive-execution' ],
    'auth': True },

  { 'name': 'pentaho-karaf-assembly' },

  { 'name': 'big-data-plugin' },

  { 'name': 'cgg',
    'fork': 'webdetails' },

  { 'name': 'cpk',
    'fork': 'webdetails' },

  { 'name': 'sparkl',
    'fork': 'webdetails',
    'deploy': True },

  { 'name': 'pentaho-cassandra-plugin' },

  { 'name': 'pdi-teradata-tpt-plugin' },

  { 'name': 'pdi-platform-utils-plugin' },

  { 'name': 'pentaho-vertica-bulkloader' },

  { 'name': 'pentaho-platform',
    'properties': [ 'skipDefault' ],
    'profile': 'platform-user-console',
    'deploy': True },

  { 'name': 'maven-parent-poms-ee',
    'auth': True },

  { 'name': 'pentaho-ee-license',
    'properties': [ 'release' ],
    'auth': True },

  { 'name': 'pentaho-platform-ee',
    'auth': True,
    'profile': 'platform-ee',
    'properties': [ 'skipDefault', 'release' ] },

  { 'name': 'jdbc-distribution-utility',
    'auth': True },

  { 'name': 'pdi-operations-mart',
    'auth': True },

  { 'name': 'pentaho-ee-chart-plugin',
    'auth': True },

  { 'name': 'pentaho-platform-plugin-geo',
    'auth': True },

  { 'name': 'pdi-ee-plugin',
    'auth': True },

  { 'name': 'pdi-jms-plugin',
    'auth': True },

  { 'name': 'pdi-scheduler-plugin',
    'auth': True },

  { 'name': 'pdi-google-docs-plugin',
    'auth': True },

  { 'name': 'pentaho-data-mining' },

  { 'name': 'pentaho-data-mining-ee',
    'auth': True },

  { 'name': 'pentaho-eula-wrap-config',
    'auth': True },

  { 'name': 'pentaho-big-data-ee',
    'auth': True },
#    'profile': 'assemblies,hdp26,cdh512,mapr520',
#    'properties': [ 'skipDefault' ] },

  { 'name': 'pdi-sap-hana-bulk-loader-plugin',
    'branch': 'master',
    'auth': True },

  { 'name': 'pentaho-r-plugin',
    'auth': True },

  { 'name': 'pentaho-splunk-plugin',
    'auth': True },

  { 'name': 'pentaho-yarn-kettle-plugin',
    'auth': True },

  { 'name': 'pdi-monitoring-plugin',
    'auth': True },

  { 'name': 'pentaho-camel-components',
    'auth': True },

  { 'name': 'pentaho-det',
    'auth': True },

  { 'name': 'pentaho-analyzer',
    'auth': True },

  { 'name': 'pentaho-analyzer',
    'modules': [ 'assemblies/paz-plugin-ce' ],
    'auth': True },

  { 'name': 'pentaho-det-ee',
    'auth': True },

  { 'name': 'pentaho-ee',
    'auth': True,
    'modules': [ 'foundry' ] },

  { 'name': 'pentaho-ee',
    'auth': True,
    'modules': [ 'platform/plugins/worker-nodes' ] },

  { 'name': 'pentaho-ee',
    'auth': True,
    'modules': [ 'data-integration/plugins/scale' ] },

  { 'name': 'pentaho-karaf-ee-assembly',
    'auth': True },

  { 'name': 'pentaho-kettle',
    'profile': 'assemblies' },

  { 'name': 'pentaho-platform',
    'profile': 'platform-assemble',
    'properties': [ 'skipDefault' ] },

  { 'name': 'pentaho-platform-ee',
    'auth': True,
    'profile': 'platform-ee-assemble',
    'properties': [ 'skipDefault' ] },

  { 'name': 'mql-editor' },

  { 'name': 'pentaho-reporting',
    'properties': [ 'specials' ] },

#  { 'name': 'pentaho-reporting',
#    'profile': 'designer' },

#  { 'name': 'pentaho-reportdesigner-ee',
#    'auth': True },

  { 'name': 'pentaho-platform-plugin-geo' },

  { 'name': 'pentaho-dashboard-chart-editor',
    'auth': True },

  { 'name': 'pentaho-platform-plugin-dashboards',
    'auth': True },

  { 'name': 'pentaho-platform-plugin-interactive-reporting',
    'auth': True },

#  { 'name': 'mondrian',
#    'modules': [ 'workbench' ] },

#  { 'name': 'pentaho-mondrianschemaworkbench-plugins' },

#  { 'name': 'mondrian',
#    'modules': [ 'assemblies' ] },

#  { 'name': 'pentaho-schema-workbench-ee',
#    'auth': True },

#  { 'name': 'pentaho-aggdesigner' },

#  { 'name': 'pentaho-aggdesigner-ee',
#    'auth': True },

#  { 'name': 'pdi-sdk-plugins' }

]
