FROM ubuntu:20.04

SHELL ["bash", "--login", "-c"]


#========================================= Docker build argument defaults
ENV APPNAME=CODE

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV FLASK_DEBUG=$FLASK_DEBUG
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000/tcp

ARG DEBIAN_FRONTEND=noninteractive
ENV PATH=/root/bin:${PATH}


RUN apt-get update

RUN echo ================================================================ INSTALL OS ESSENTIALS
RUN apt-get --yes install apt-utils
RUN apt-get --yes install curl
RUN apt-get --yes install wget
RUN apt-get --yes install software-properties-common


# YES YES, I KNOW YOU COULD USE A READY-MADE OFFICIAL PYTHON IMAGE
# THING IS - I WANT TO USE A VERY SPECIFIC LINUX DISTRO AND VERSION,
# SO I MAKE THE IMAGE MYSELF
RUN echo ================================================================ INSTALL PYTHON
RUN apt-get --yes install python3
RUN apt-get --yes install python3-pip


RUN echo ================================================================ SETTING/MAKING PATHS
ARG APPHOME=/root/PYTHONDEV/${APPNAME}
ENV APPHOME=$APPHOME

RUN mkdir -p $APPHOME

RUN echo ================================================================ GETTING CODE FROM HOST OS
COPY . $APPHOME


RUN echo ================================================================ RUNNING SERVICES
RUN echo "#!/usr/bin/env bash" >> /root/bin/start_container_services.sh && \
    echo "set -x" >> /root/bin/start_container_services.sh && \
    echo "cd $APPHOME" >> /root/bin/start_container_services.sh && \
    echo "flask run">> /root/bin/start_container_services.sh && \
    chmod +x /root/bin/start_container_services.sh


RUN echo ================================================================ FINISHED
WORKDIR ${APPHOME}
CMD /root/bin/start_container_services.sh

# EOF
