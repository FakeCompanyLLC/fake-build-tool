build=true
if [ -f "last_commit.txt" ]; then
  echo "Getting latest commit"
  LAST_COMMIT=$(cat last_commit.txt)
  if [ -d "fake-build-tool" ]; then
    cd fake-build-tool
    git fetch
    git reset --hard origin/master
    COMMIT=$(git rev-parse HEAD)
    echo $COMMIT
    cd ..
    if [ "$COMMIT" == "$LAST_COMMIT" ]; then
      echo "Build is latest, skipping..."
      build=false
    else
      echo "Build is stale, building..."
    fi
  fi
fi
if [ "$build" = true ]; then
  if [ ! -d "fake-build-tool" ]; then
    git clone --depth=1 https://github.com/FakeCompanyLLC/fake-build-tool.git
  else
    cd fake-build-tool
    git fetch
    git reset --hard origin/master
    cd ..
  fi
  cd fake-build-tool
  COMMIT=$(git rev-parse HEAD)
  echo "$COMMIT" > ../last_commit.txt
  cd client
  npm install
  ng build
  cd ..
  cd services
  npm install
  cd ../..
fi
docker stop fbt-ui > /dev/null 2>&1
docker rm fbt-ui > /dev/null 2>&1
docker build -t schwingman:latest .
docker run --name fbt-ui --net fbt-net -d -it -p 80:80 schwingman:latest
