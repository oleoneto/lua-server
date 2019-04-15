#!/usr/bin/env bash
# Notify to Slack

PAYLOAD="$1" && curl -X POST -H 'Content-type: application/json' --data '{"text": "$PAYLOAD" }' https://hooks.slack.com/services/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
