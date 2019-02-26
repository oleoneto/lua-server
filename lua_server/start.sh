#!/bin/sh

# echo ">>> Collecting static files to specified volume..."
python manage.py collectstatic --no-input


if [ ! -f $PROJECT_ROOT/.app_auth ]; then
	# WARNING: if using a custom AUTH_USER, ensure the app
	# for the custom AUTH_USER is migrated first.
	# echo ">>> Running migrations in 'core' for AUTH_USER"
	python manage.py makemigrations core && \
	python manage.py migrate core && \
	date > $PROJECT_ROOT/.app_auth && \
	date > $PROJECT_ROOT/.app_db
fi


# echo ">>> Running general project migrations..."
python manage.py migrate

exec "$@"
