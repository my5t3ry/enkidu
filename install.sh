#!/usr/bin/env bash
pip3 install \
  pillow \
  google-auth \
  pygments \
  google-auth \
  google-auth-httplib2 \
  google-api-python-client \
  google-api-python-client \
  simpleeval \
  jsbeautifier \
  whois \
  APScheduler \
  shortuuid \
  quote \
  flask \
  uuid

mkdir -p ~/.enkidu/assets/dist
cp etc/defaultsettings.json ~/.enkidu/
cp etc/help.txt ~/.enkidu/
