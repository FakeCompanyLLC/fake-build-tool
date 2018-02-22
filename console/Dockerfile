FROM ubuntu:latest
MAINTAINER Benjamin Morrise <bmorrise@gmail.com>>

# make sure the package repository is up to date
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
RUN "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y mongodb-org
RUN apt-get install -y nginx
RUN apt-get install -y vim
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN mkdir -p /app/client
RUN mkdir -p /app/services
ADD client/dist /app/client
ADD services /app/services
ADD default /etc/nginx/sites-enabled
ADD init.sh /init.sh
RUN chmod +x /init.sh

#ENTRYPOINT bash
ENTRYPOINT /init.sh; bash
