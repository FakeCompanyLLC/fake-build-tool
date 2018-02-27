# name, url, modules, cmd
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
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '9c55c1ad0b304d5ae926c80adc4db7ccc9f104a4' ],
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'mondrian',
#    'fork': 'lucboudreau',
#    'branch': 'mondrian2579',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'pentaho-reporting',
    'cmd': ['mvn -Dpentaho.public.snapshot.repo=http://172.17.0.1:8081/nexus/content/repositories/snapshots --non-recursive clean install deploy -DskipTests'] },

  { 'name': 'metastore' },

  { 'name': 'pentaho-reporting',
    'modules': [ 'libraries' ],
    'properties': [ 'libraries' ] },

  { 'name': 'pentaho-registry',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '78f594fdc4486a4363c16c2f55b1ef4e0684017b' ]
  },


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

  { 'name': 'pentaho-mongo-utils',
    'remotes': [ 'pentaho-mracine' ],
    'cherry-picks': [ '23918babf8e2ec0fa07347de5b4a85f74f9e2b4c' ] },

  { 'name': 'pentaho-mongodb-plugin',
    'remotes': [ 'pentaho-mracine' ],
    'cherry-picks': [ '396a7767576aee939600de31fe7d9c7587b2d0d1' ] },

  { 'name': 'pentaho-metaverse' },

  { 'name': 'pentaho-commons-database',
    'modules': ['gwt'] },

  { 'name': 'modeler' },

  { 'name': 'cpf',
    'fork': 'webdetails' },

  { 'name': 'ccc',
    'fork': 'webdetails',
    'cmd': ['ant -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots clean-all clean-js dist publish publish-local'] },

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
#    'fork': 'lucboudreau',
#    'branch': 'pdi14064',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '529acb2a74ec3a79eba6c11b756f8a1716999cfc' ],
    'modules': [ 'plugins' ],
    'profile': 'highdeps' },

  { 'name': 'data-access' },

  { 'name': 'cda',
    'fork': 'webdetails'
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ 'd48b31e1063cf1d066176b4cb7d2c05e47db8ab6' ]
  },

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

  { 'name': 'pdi-dataservice-server-plugin',
    'remotes': [ 'pentaho-mracine' ],
    'cherry-picks': [ '8161d8cb94f8090f3df7da05a764c20d4d0d1666' ] },

  { 'name': 'pentaho-data-refinery' },

  { 'name': 'big-data-plugin',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '1a363b58fb56fd433adcc460eb4c59359696c162' ],
    'cmd': ['mvn --non-recursive clean install -DskipTests'] },

  { 'name': 'big-data-plugin',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '1a363b58fb56fd433adcc460eb4c59359696c162' ],
    'properties': [ 'featuresOnly' ] },

  { 'name': 'pentaho-ee',
    'remotes': [ 'mdamour1976' ],
#    'cherry-picks': [ '955e37095916d6f8170b7a6583ebdd6f851d2de1' ],
#    'rebases': [ 'mdamour1976/resolvefix' ],
    'modules': [ 'adaptive-execution' ],
    'auth': True },

  { 'name': 'pentaho-karaf-assembly',
    'remotes': [ 'pentaho-mracine' ],
    'cherry-picks': [ '69f245101e64d04cee4d2f48395db4cdf5d8ebad' ] },

  { 'name': 'big-data-plugin',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '1a363b58fb56fd433adcc460eb4c59359696c162' ],
  },

#  { 'name': 'pentaho-ee',
#    'remotes': [ 'mdamour1976' ],
#    'cherry-picks': [ '955e37095916d6f8170b7a6583ebdd6f851d2de1' ],
#    'rebases': [ 'mdamour1976/resolvefix' ],
#    'auth': True },

  { 'name': 'cgg',
    'fork': 'webdetails' },
#    'modules': ['cgg-core'] },

#  { 'name': 'cgg',
#    'fork': 'webdetails' },

#  { 'name': 'cpk',
#    'fork': 'webdetails',
#    'modules': ['cpk-core'] },

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
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '9c55c1ad0b304d5ae926c80adc4db7ccc9f104a4' ],
    'properties': [ 'skipDefault' ],
    'profile': 'platform-user-console',
    'deploy': True },

  # begin attempt to build assembly-ee
  # version.for.license=7.1-SNAPSHOT
  { 'name': 'pentaho-ee-license',
    'auth': True,
    'modules': [ 'pentaho-ee-license-core' ],
    'cmd': [ 'ant -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots clean-all resolve jar obfuscate publish-local publish-nojar' ] },

  { 'name': 'pentaho-ee-license',
    'auth': True,
    'modules': [ 'pentaho-ee-mock-license' ] },

  { 'name': 'maven-parent-poms-ee',
    'auth': True },

  { 'name': 'pentaho-metadata-ee',
    'auth': True },

  { 'name': 'pentaho-ee-license',
    'auth': True,
    'modules': [ 'pentaho-ee-license-installer' ],
    'cmd': [ 'ant -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots -buildfile assembly.xml clean-all resolve assemble package-zip create-pom publish-nojar' ] },

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

#  { 'name': 'pentaho-platform-plugin-jpivot' },
#  { 'name': 'pentaho-platform-plugin-jpivot',
#    'cmd': ['ant -Divy.repository.publish=http://172.17.0.1:8081/nexus/content/repositories/snapshots -buildfile build-disabled.xml clean-all resolve dist publish-local'] },

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

  # base, assemblies
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

#  { 'name': 'pentaho-mongolap',
#    'auth': True },

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
    'remotes': [ 'mdamour1976' ],
#    'cherry-picks': [ '955e37095916d6f8170b7a6583ebdd6f851d2de1' ],
#    'rebases': [ 'mdamour1976/resolvefix' ],
    'auth': True,
    'modules': [ 'foundry' ] },

  { 'name': 'pentaho-ee',
    'remotes': [ 'mdamour1976' ],
#    'cherry-picks': [ '955e37095916d6f8170b7a6583ebdd6f851d2de1' ],
#    'rebases': [ 'mdamour1976/resolvefix' ],
    'auth': True,
    'modules': [ 'platform/plugins/worker-nodes' ] },

  { 'name': 'pentaho-karaf-ee-assembly',
    'auth': True },

  { 'name': 'pentaho-kettle',
#    'fork': 'lucboudreau',
#    'branch': 'pdi14064',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '529acb2a74ec3a79eba6c11b756f8a1716999cfc' ],
    'profile': 'assemblies' },

  { 'name': 'pentaho-platform',
#    'remotes': [ 'axelguiloff' ],
#    'cherry-picks': [ '9c55c1ad0b304d5ae926c80adc4db7ccc9f104a4' ],
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
#    'fork': 'mdamour1976',
#    'branch': 'mdd',
#    'remotes': [ 'mdamour1976' ],
#    'cherry-picks': [ 'e40376710554ec44c68dabbbd6147b004334d58c' ],
    'auth': True },

  { 'name': 'pentaho-platform-plugin-interactive-reporting',
    'auth': True },

#  { 'name': 'pentaho-ee',
#    'remotes': [ 'mdamour1976' ],
#    'cherry-picks': [ '955e37095916d6f8170b7a6583ebdd6f851d2de1' ],
#    'rebases': [ 'mdamour1976/resolvefix' ],
#    'auth': True,
#    'modules': [ 'data-integration/assemblies/client' ],
#    'cmd': [ 'ant -f assembly.xml clean-all resolve di-package' ] },

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
