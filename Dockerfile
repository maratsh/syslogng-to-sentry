FROM debian:jessie

RUN apt-get update -qq
RUN apt-get install apt-utils -y
RUN apt-get install -y \
    wget \
    gnupg2

RUN wget -qO - https://download.opensuse.org/repositories/home:/laszlo_budai:/syslog-ng/Debian_8.0/Release.key | apt-key add -
RUN echo 'deb http://download.opensuse.org/repositories/home:/laszlo_budai:/syslog-ng/Debian_8.0 ./' | tee --append /etc/apt/sources.list.d/syslog-ng-obs.list

RUN apt-get update -qq && apt-get install -y \
    syslog-ng
RUN apt-get install python python2.7 libpython2.7 python-pip -y
RUN pip install raven

RUN ldconfig


EXPOSE 6128/tcp

ENV PYTHONPATH $PYTHONPATH:/etc/syslog-ng/

ENTRYPOINT ["/usr/sbin/syslog-ng", "-F"]
