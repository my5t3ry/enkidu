#!/usr/bin/env bash
curl -vX POST http://localhost:4343 -d @slash_me.json \
--header "Content-Type: application/json"
