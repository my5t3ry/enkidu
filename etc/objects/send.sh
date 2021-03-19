#!/usr/bin/env bash
curl -vX POST http://localhost:4343 -d @slash_public.json \
--header "Content-Type: application/json"
