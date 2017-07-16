syslog-ng to sentry destination
===============================

## Requirements

* syslog-ng 3.10
* python-2.7
* python-raven 6.1.0

## Installation

* Install Syslog-ng with syslog-ng python destination module
* Place sng2sentry.py somewhere in system
* set PYTHONPATH for syslog-ng to the sng2sentry
* Create project in sentry and copy DSN
* Configure Sentry destination by syslog-ng.conf.example
* Run syslog-ng

## syslog to sentry level mapping

Syslog and sentry has different level mapping

This driver maps syslog level that way:

```
debug (the least serious) 7
info 5-6
warning 4
error 3
fatal (the most serious) 0-2
```
