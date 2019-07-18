FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq && apt-get install build-essential g++ flex bison gperf ruby perl \
  mysql-client \
  libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
  libpng-dev libjpeg-dev python libx11-dev libxext-dev -y
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
