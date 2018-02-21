/etc/init.d/postgresql start
/usr/sbin/sshd

#export JAVA_HOME=/pentaho/jdk1.8.0_151
#export PATH=$JAVA_HOME/bin:$PATH

cd /pentaho/pentaho-server
./start-pentaho-debug.sh -q
tail -f /pentaho/pentaho-server/tomcat/logs/catalina.out &
#tail -f /pentaho/pentaho-server/tomcat/logs/catalina.out
