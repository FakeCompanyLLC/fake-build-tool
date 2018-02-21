FROM      ubuntu:14.04
MAINTAINER Michael D'Amour <mdamour@pentaho.com>

# make sure the package repository is up to date
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get -y -q install python-software-properties software-properties-common
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8 LC_MESSAGES=POSIX


RUN apt-get -y -q install unzip nano git python python-pip wget curl
RUN apt-get -y -q install openssh-client openssh-server
#RUN add-apt-repository -y "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"
#RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
ADD apt.postgresql.org.sh /pentaho/apt.postgresql.org.sh
RUN /pentaho/apt.postgresql.org.sh
RUN apt-get -y -q install postgresql-9.6 postgresql-client-9.6 postgresql-contrib-9.6

RUN pip uninstall requests; pip install requests


# install java7
#RUN add-apt-repository -y ppa:webupd8team/java
#RUN apt-get update
#RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
#RUN apt-get install -y oracle-java7-installer

# install java8
# BROKEN as of 10/18/2017
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer

#RUN add-apt-repository -y ppa:webupd8team/java
#RUN apt-get update
#RUN echo oracle-java9-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
#RUN apt-get install -y oracle-java9-installer




RUN mkdir /var/run/sshd
RUN echo 'root:pentaho' |chpasswd
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config
RUN useradd pentaho
RUN echo 'pentaho:pentaho' | chpasswd
RUN mkdir -p /pentaho
ADD pg_hba.conf /pentaho/pg_hba.conf
ADD install.sh /pentaho/install.sh
ADD startup.sh /pentaho/startup.sh
ADD qat_smoker.py /pentaho/qat_smoker.py

#ADD jdk-8u151-linux-x64.tar.gz /pentaho/

EXPOSE 22 5432 8044 8080 9001
#ENTRYPOINT pip --version python --version ; python /pentaho/qat_smoker.py
ENTRYPOINT bash /pentaho/install.sh; bash /pentaho/startup.sh; python /pentaho/qat_smoker.py
#ENTRYPOINT bash
