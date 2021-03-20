#!/usr/bin/env bash
pip3 install \
  pillow \
  google-auth \
  pygments \
  google-auth \
  google-auth-httplib2 \
  google-api-python-client \
  google-api-python-client \
  jsonschema \
  simpleeval \
  flask \
  uuid

mkdir -p ~/.enkidu/assets/img
mkdir -p ~/.enkidu/assets/html
cp etc/defaultsettings.json ~/.enkidu/
