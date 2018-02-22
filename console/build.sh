docker stop fbt-ui
docker rm fbt-ui
docker build -t schwingman:latest .
docker run --name fbt-ui --net fbt-net -d -it -p 80:80 schwingman:latest --rm -v `pwd`/db:/data/db
