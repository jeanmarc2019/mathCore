FROM ubuntu:16.04

MAINTAINER Jean-Marc Daviau-Williams

# Python/Flask stuff
RUN apt-get update --fix-missing && apt-get install -y software-properties-common python3 python3-pip apache2 libapache2-mod-wsgi && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip3 install pandas==0.23
RUN pip3 install MIDIutil
# RUN pip3 install flask_SQLAlchemy
# RUN pip3 install newspaper3k
# RUN pip3 install mysql-connector-python
# RUN pip3 install us
# RUN pip3 install nltk
# RUN pip3 install newsapi-python
# RUN pip3 install textblob
# RUN pip3 install flask
# RUN pip3 install flask-restful
# RUN pip3 install ConfigParser
# RUN pip3 install https://github.com/mitsuhiko/flask/tarball/master
# Enables Apache2 module required for serving API
RUN a2enmod wsgi

# Apache2 Defaults
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/log/apache2
ENV APACHE_PID_FILE /etc/apache2/pid.txt
COPY ./docker/app/apache2.conf /etc/apache2/apache2.conf
RUN chown -R www-data:www-data /var/www/html

# Frontend
EXPOSE 80

# API
EXPOSE 5000

# Ties docker container with Apache2
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]