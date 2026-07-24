#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

echo "Creating superuser..."

python manage.py createsuperuser --noinput

echo "Finished creating superuser."