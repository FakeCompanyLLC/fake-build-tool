FROM      ubuntu:latest
MAINTAINER Michael D'Amour <mdamour@pentaho.com>

# make sure the package repository is up to date
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get -y -q install python-software-properties software-properties-common locales
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8 LC_MESSAGES=POSIX

#RUN apt-get -y -q install postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3
RUN apt-get -y -q install unzip nano git python python-pip wget curl
RUN pip uninstall requests; pip install requests
RUN apt-get -y -q install openssh-client openssh-server

# install java7
#RUN add-apt-repository -y ppa:webupd8team/java
#RUN apt-get update
#RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
#RUN apt-get install -y oracle-java7-installer
# install java8
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer
# install java9
#RUN add-apt-repository -y ppa:webupd8team/java
#RUN apt-get update
#RUN echo oracle-java9-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
#RUN apt-get install -y oracle-java9-installer

#RUN apt-get install python-software-properties
#RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
#RUN curl -sL https://deb.nodesource.com/setup_0.10 | sudo -E bash -
#RUN apt-get install nodejs

# setup ssh
RUN mkdir /var/run/sshd
RUN echo 'root:pentaho' |chpasswd
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config

# install phantomjs pre-reqs
RUN apt-get -y -q install build-essential chrpath libssl-dev libxft-dev
RUN apt-get -y -q install libfreetype6 libfreetype6-dev
RUN apt-get -y -q install libfontconfig1 libfontconfig1-dev

RUN apt-get -y -q install sudo
#RUN curl -sL https://deb.nodesource.com/setup_0.10 | sudo -E bash -
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN apt-get -y -q install nodejs
RUN npm install -g requirejs
RUN npm install -g jsmin
RUN npm install -g karma
RUN npm install -q phantomjs-prebuilt


RUN mkdir /pentaho
ADD subfloor.xml /pentaho/subfloor.xml
ADD settings.xml /pentaho/settings.xml
ADD ivysettings.xml /pentaho/ivysettings.xml
ADD publish.xml /pentaho/publish.xml
ADD apache-ant-1.10.1.tar.gz /pentaho
ADD apache-maven-3.3.9-bin.tar.gz /pentaho
ADD ant-contrib-1.0b3.jar /pentaho
ADD ivy-2.4.0.jar /pentaho
ADD pentaho-ee-ant-tasks-1.1.0.tar /pentaho
#ADD phantomjs-2.1.1-linux-x86_64.tar.gz /pentaho

ADD override.properties /pentaho/override.properties
ADD buildlib.py /pentaho/buildlib.py

ADD build-all.sh /pentaho/build-all.sh
ADD build-all.py /pentaho/build-all.py
ADD projects.py /pentaho/projects.py
ADD env.sh /pentaho/env.sh
ADD gitjson.py /pentaho/gitjson.py
ADD slack.py /pentaho/slack.py

EXPOSE 22
#ENTRYPOINT bash
ENTRYPOINT /usr/sbin/sshd; bash /pentaho/build-all.sh
