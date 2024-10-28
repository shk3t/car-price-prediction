. ./.env

python manage.py migrate

gunicorn --workers=2 --bind=$HOST:$ML_PORT --env DJANGO_SETTINGS_MODULE=core.settings core.wsgi