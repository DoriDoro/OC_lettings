generate_secret_key:
	@python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'

setup_local_env:
	@export DJANGO_SETTINGS_MODULE=oc_lettings_site.settings-local-template

install:
	@python -m pip install --upgrade pip
	@pip install -r requirements.txt
	@python manage.py migrate
	@gunicorn oc_lettings_site.wsgi:application
