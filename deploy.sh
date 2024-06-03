python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn -b 0.0.0.0:8000 oc_lettings_site.wsgi:application
