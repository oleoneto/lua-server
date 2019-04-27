#!/usr/bin/env bash

python manage.py makemigrations core && \
python manage.py migrate core && \
python manage.py migrate --noinput && \
python manage.py collectstatic --noinput && \
curl -X POST -H 'Content-type: application/json' --data '{"text": "Message from Lua" }' https://hooks.slack.com/services/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 && \
./.notify.sh "Lua LMS is live!!"