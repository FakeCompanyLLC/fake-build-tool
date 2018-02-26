FROM  pentaho-build:8.1.0.0-SNAPSHOT

#Install for UI
RUN apt-get install -y -q vim rabbitmq-server
RUN pip install pika; pip install Flask; pip install psutil
ADD init.sh /init.sh
RUN chmod +x /init.sh
ADD commands.py /pentaho/commands.py

ENTRYPOINT /init.sh; /usr/sbin/sshd; bash
