# Use an official Python runtime as a parent image
FROM ubuntu:14.04
FROM python:3.5.2-slim

RUN apt-get update  && apt-get install -y apache2 apache2-dev net-tools curl vim 
RUN pip install mod_wsgi 
RUN apachectl configtest
RUN mod_wsgi-express module-config
RUN mod_wsgi-express install-module


RUN mkdir /etc/tokenleader
COPY . /etc/tokenleader/
RUN chmod 644 /etc/tokenleader/id_rsa

COPY ./wsgi.load /etc/apache2/mods-available/
COPY ./wsgi.conf /etc/apache2/mods-available/
RUN ln -s /etc/apache2/mods-available/wsgi.load  /etc/apache2/mods-enabled/wsgi.load
RUN ln -s /etc/apache2/mods-available/wsgi.conf  /etc/apache2/mods-enabled/wsgi.conf
COPY ./tokenleader-apache.conf /etc/apache2/sites-enabled/
COPY ./ports.conf /etc/apache2/
COPY ./app.wsgi /usr/local/lib/python3.5/site-packages/tokenleader/
#RUN ls -l /etc/tokenleader
RUN  a2enmod ssl 
RUN apachectl configtest

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org tokenleader
RUN tokenleader-auth -u user1 -p user1 --url https://localhost:5001
RUN adminops initdb 
RUN  adminops   add  org   -n org1  
RUN  adminops   add  ou   -n ou1 
RUN  adminops   add  dept   -n  dept1  
RUN  adminops   addwfc -n wfc1 --wfcorg org1 --wfcou ou1 --wfcdept dept1 	 
RUN  adminops   list  wfc  -n wfc1
RUN  adminops   add  role  -n role1  	  
RUN  adminops adduser -n user1 --password user1 --emailid user1 --rolenames role1  --wfc wfc1
RUN  adminops  addservice  -n tokenleader --password tokenleader --urlint localhost:5001



# Make port 80 available to the world outside this container
EXPOSE 5001


#CMD ["tokenleader-start"]

RUN apachectl configtest 

RUN service apache2 start


CMD ["apachectl", "-f", "/etc/apache2/apache2.conf", "-D", "FOREGROUND" , "-X"]

#CMD ["cat"]
