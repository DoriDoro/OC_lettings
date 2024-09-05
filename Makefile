generate_secret_key:
	python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'

virtual_env_linux:
	python3 -m venv venv
	venv/bin/activate

virtual_env_windows:
	python3 -m venv venv
	venv\Scripts\activate

setup_local_env:
	export DJANGO_SETTINGS_MODULE=oc_lettings_site.settings-local-template

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r docs/docs_requirements.txt
	python manage.py migrate
	gunicorn oc_lettings_site.wsgi:application

# this command: `pull_docker_image_jq` requires installation of curl and jq on your local machine
# $ sudo apt update && sudo apt install -y curl && sudo apt install -y jq
# $ sudo apt update ; sudo apt install -y curl ; sudo apt install -y jq
pull_docker_image_jq:
	docker login; \
    image="doridoro/oc_lettings_site"; \
    tag=$$(curl -s "https://registry.hub.docker.com/v2/repositories/$$image/tags/" | jq -r '.results | sort_by(.last_updated) | last.name'); \
    if [ -z "$$tag" ]; then \
        echo "Error: Failed to fetch Docker image tag."; \
        exit 1; \
    fi; \
    docker pull "$$image:$$tag"

# this command: `pull_docker_image_python` requires installation of curl on your local machine
# $ sudo apt update && sudo apt install -y curl
# $ sudo apt update ; sudo apt install -y curl
pull_docker_image_python:
	docker login; \
	image="doridoro/oc_lettings_site"; \
	tag=$$(curl -s "https://registry.hub.docker.com/v2/repositories/$$image/tags/" | python3 -c "import sys, json; print(max(json.load(sys.stdin)['results'], key=lambda x: x['last_updated'])['name'])"); \
	if [ -z "$$tag" ]; then \
	    echo "Error: Failed to fetch Docker image tag."; \
	    exit 1; \
	fi; \
	docker pull "$$image:$$tag"

# run the pulled docker image locally
run_docker_image:
	image="doridoro/oc_lettings_site"; \
	tag=$$(curl -s "https://registry.hub.docker.com/v2/repositories/$$image/tags/" | python3 -c "import sys, json; print(max(json.load(sys.stdin)['results'], key=lambda x: x['last_updated'])['name'])"); \
	if [ -z "$$tag" ]; then \
	    echo "Error: Failed to fetch Docker image tag."; \
	    exit 1; \
	fi; \
	docker run -e SECRET_KEY=secret -e ALLOWED_HOSTS='*' -e DEBUG=True -p 8000:8000 "$$image:$$tag" python manage.py collectstatic && gunicorn oc_lettings_site.wsgi:application

setup_install: setup_local_env install
virtual_linux_setup_install: virtual_env_linux setup_local_env install
virtual_windows_setup_install: virtual_env_windows setup_local_env install
