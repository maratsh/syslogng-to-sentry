#!/usr/bin/env bash

docker run -it  -v "$PWD/syslog-ng.conf":/etc/syslog-ng/syslog-ng.conf -v "$PWD/sng2sentry.py":/etc/syslog-ng/sng2sentry.py -v "$PWD/tmp":/tmp/  syslog-ng-to-sentry:latest   syslog-ng --no-caps -F -rte
