generate_secret_key:
	@python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'

virtual_env_linux:
	@python3 -m venv venv
	@venv/bin/activate

virtual_env_windows:
	@python3 -m venv venv
	@venv\Scripts\activate

setup_local_env:
	@export DJANGO_SETTINGS_MODULE=oc_lettings_site.settings-local-template

install:
	@python -m pip install --upgrade pip
	@pip install -r requirements.txt
	@pip install -r docs/docs_requirements.txt
	@python manage.py migrate
	@gunicorn oc_lettings_site.wsgi:application

setup_install: setup_local_env install
virtual_linux_setup_install: virtual_env_linux setup_local_env install
virtual_windows_setup_install: virtual_env_windows setup_local_env install
