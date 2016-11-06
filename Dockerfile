FROM ubuntu:14.04
MAINTAINER Mike Faraponov "mikefaraponov@gmail.com"
RUN  apt-get update && apt-get install --force-yes -y \
     python-pip python-dev build-essential
COPY . /home/pysql
WORKDIR /home/pysql
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-m"]
CMD ["pysql"]
EXPOSE 1337