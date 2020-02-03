#!/usr/bin/env bash

curl -X POST -H 'Content-type: application/json' --data '{"text": "Lua LMS deployed successfully" }' https://hooks.slack.com/services/$SLACK_TOKEN
