#export JAVA_HOME=/pentaho/jdk1.8.0_151
#export PATH=$JAVA_HOME/bin:$PATH


cd /pentaho

# fetch latest dev licenses
wget --user=$BOX_USER --password=$BOX_PASSWORD "ftp://ftp.box.com/CI/DEV_LICENSES/Pentaho Reporting Enterprise Edition.lic"
wget --user=$BOX_USER --password=$BOX_PASSWORD "ftp://ftp.box.com/CI/DEV_LICENSES/Pentaho PDI Enterprise Edition.lic"
wget --user=$BOX_USER --password=$BOX_PASSWORD "ftp://ftp.box.com/CI/DEV_LICENSES/Pentaho Hadoop Enterprise Edition.lic"
wget --user=$BOX_USER --password=$BOX_PASSWORD "ftp://ftp.box.com/CI/DEV_LICENSES/Pentaho Dashboard Designer.lic"
wget --user=$BOX_USER --password=$BOX_PASSWORD "ftp://ftp.box.com/CI/DEV_LICENSES/Pentaho BI Platform Enterprise Edition.lic"
wget --user=$BOX_USER --password=$BOX_PASSWORD "ftp://ftp.box.com/CI/DEV_LICENSES/Pentaho Analysis Enterprise Edition.lic"

# fetch build
cp /git-storage/pentaho/pentaho-platform-ee/assemblies/pentaho-server-ee/target/pentaho-server-ee-$RELEASE_VERSION.zip .
cp /git-storage/pentaho/pentaho-analyzer/assemblies/paz-plugin-ee/target/paz-plugin-ee-$RELEASE_VERSION.zip .
cp /git-storage/pentaho/pentaho-platform-plugin-dashboards/assemblies/plugin/target/pdd-plugin-ee-$RELEASE_VERSION.zip .
cp /git-storage/pentaho/pentaho-platform-plugin-interactive-reporting/assemblies/plugin/target/pir-plugin-ee-$RELEASE_VERSION.zip .

# extract server
unzip -q pentaho-server*

# install dev licenses
./license-installer/install_license.sh install -q /pentaho/*.lic

# setup postgres, populate with scripts
echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf
cd /pentaho/pentaho-server/data/postgresql
/etc/init.d/postgresql start
cp /pentaho/pg_hba.conf /etc/postgresql/9.6/main/pg_hba.conf
/etc/init.d/postgresql restart
psql -U postgres -f create_jcr_postgresql.sql
psql -U postgres -f create_quartz_postgresql.sql
psql -U postgres -f create_repository_postgresql.sql
psql -U postgres -f pentaho_mart_postgresql.sql
psql -U postgres -f pentaho_logging_postgresql.sql
/etc/init.d/postgresql stop

cd /pentaho/pentaho-server/pentaho-solutions/system
unzip -qo /pentaho/paz*
unzip -qo /pentaho/pdd*
unzip -qo /pentaho/pir*

# force platform to not prompt user at first startup
cd /pentaho/pentaho-server
rm promptuser.sh
