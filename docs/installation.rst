Installation
============

Possibility 1:
--------------

Docker image
------------

Docker cli or desktop has to be installed on your machine.

# replace <username> with your username
$ docker login -u <username>
Enter your password/Docker Hub token and login to Docker

# replace <flag>
$ docker pull doridoro/oc_lettings_site:<flag>



pull the docker image and run the container
SECRET_KEY, DEBUG, ALLOWED_HOSTS and -b 0:0:0:0:8000 for gunicorn


Possibility 2:
--------------

Clone the GitHub repository
---------------------------

1.  `$ git clone https://github.com/DoriDoro/OC_lettings.git`
2.  `$ cd OC_lettings`

Create a SECRET_KEY
-------------------

choose one of these two options:
1.1 `$ make generate_secret_key`
1.2 create and set the `SECRET_KEY`
choose 3.1 or 3.2 and replace the `SECRET_KEY` in file: oc_lettings_site/settings-local-template

Install all dependencies
------------------------

choose a simple setup including creating a virtual environment, setup the DJANGO_SETTINGS_MODULE
in terminal and install all dependencies:
1.1 for Linux/Mac: `$ make virtual_linux_setup_install`
1.2 for Windows: `$ make virtual_windows_setup_install`

or create your own virtual environment:
1.3 and use `$ make setup_install` to set the
    `DJANGO_SETTINGS_MODULE` in terminal and install all
1.4 and set the `DJANGO_SETTINGS_MODULE=oc_lettings_site.settings-local-template` install with
    `$ pip install -r requirements.txt`

Run the server
--------------

1. `$ python manage.py runserver`
2. `$ gunicorn oc_lettings_site.wsgi:application`
and navigate to http://127.0.0.1:8000 in your browser
