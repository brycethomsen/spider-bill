FROM ubuntu
MAINTAINER Bryce Thomsen
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
RUN pip3 install scrapy ipython
