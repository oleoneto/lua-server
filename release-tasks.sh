#!/usr/bin/env bash

python manage.py makemigrations core && \
python manage.py migrate core && \
python manage.py migrate --noinput && \
/.notify.sh "Lua LMS is live!!"