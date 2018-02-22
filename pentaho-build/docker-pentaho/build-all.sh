source /pentaho/env.sh

git config --global user.email "mdamour@pentaho.com"
git config --global user.name "Michael D'Amour"

cd /pentaho/git-storage

mkdir -p /root/.subfloor/ivy
mkdir -p /root/.subfloor/ant-contrib
mkdir -p /root/.m2
mkdir -p /root/.ant/lib

cp /pentaho/ivy-2.4.0.jar /root/.subfloor/ivy/ivy.jar
cp /pentaho/ivy-2.4.0.jar /root/.ant/lib/ivy.jar
cp /pentaho/ant-contrib*.jar /root/.subfloor/ant-contrib/
cp -Rf /pentaho/pentaho-ee-ant-tasks-1.1.0 /root/.subfloor/

cp /pentaho/settings.xml /root/.m2/

cd /pentaho
python build-all.py

EXIT_STATUS=$?
exit $EXIT_STATUS
