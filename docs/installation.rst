Installation options
====================

I have implemented several ``make`` commands to streamline various aspects of our Django project setup
and development workflow:

    ``generate_secret_key``:
        This command generates a new secret key for our Django application. The secret key is
        crucial for securely handling sessions and cryptographic signing in our project.

    ``virtual_env_linux``:
        This command is designed for Linux and macOS environments. It sets up a virtual environment
        where Python dependencies can be installed separately from the system's Python
        installation. This helps maintain clean and isolated development environments.

    ``virtual_env_windows``:
        Similar to virtual_env_linux, this command creates a virtual environment tailored for
        Windows systems. It ensures consistent dependency management and isolates Python packages
        specific to our project.

    ``setup_local_env``:
        This command sets the DJANGO_SETTINGS_MODULE environment variable, which specifies the
        settings module Django should use. It's essential for configuring our Django application
        to use the correct settings file (settings.py) based on the environment (development,
        staging, production, etc.).

    ``install``:
        This comprehensive command automates several critical steps:
            Updates pip to the latest version to ensure dependency management is up-to-date.
            Installs all project dependencies listed in requirements.txt or Pipfile using pip.
            Executes Django's database migration (``python manage.py migrate``), ensuring the
            database schema is synchronized with the current state of our Django models.
            Starts the Django server using gunicorn, a production-ready WSGI server, to serve our
            application.

These ``make`` commands collectively streamline our development process, ensuring consistency and
efficiency across different operating systems and project environments. By automating these tasks,
we reduce manual errors and accelerate the setup and deployment of our Django application.

***************************************************************************************************

Possibility 1: Retrieving the Latest Docker Image
-------------------------------------------------

`Ensure you have your Docker Hub login credentials ready.`

Login to Docker Hub and pull the Latest Docker Image: ::

$ make pull_docker_image

Verify the Pulled Image and get the ``TAG``: ::

$ docker images

Run the Docker Container and replace <tag> with ``TAG`` from command $ docker images::

$ docker run -e SECRET_KEY=secret -p 8000:8000 doridoro/oc_lettings_site:<tag> python manage.py collectstatic && gunicorn oc_lettings_site.wsgi:application

***************************************************************************************************

Possibility 2: Clone the GitHub repository
------------------------------------------

**1) Clone the GitHub repository**

in terminal: ::

$ git clone https://github.com/DoriDoro/OC_lettings.git
$ cd OC_lettings


**2) Create a SECRET_KEY**

create a ``SECRET_KEY`` with command: ::

$ make generate_secret_key

and replace the ``SECRET_KEY`` in file: oc_lettings_site/settings-local-template


**3) Install all dependencies**

choose a simple setup including creating a virtual environment, setup the
``DJANGO_SETTINGS_MODULE`` in terminal and install all dependencies:

3.1) for Linux/Mac: ::

$ make virtual_linux_setup_install

**Description:** This command is tailored for Linux and macOS environments. It first sets up a
virtual environment to isolate Python dependencies, then configures the local environment variables
(``DJANGO_SETTINGS_MODULE``), and finally installs all project dependencies, updates pip,
migrates the database, and starts the Django server with gunicorn.

**Usage:** Ideal for ensuring a clean and isolated development environment on Linux and macOS
systems, enhancing dependency management and consistency across different setups.

3.2) for Windows: ::

$ make virtual_windows_setup_install

**Description:** Designed for Windows environments, this command initiates a virtual environment to
isolate Python dependencies, sets up the local environment variables (``DJANGO_SETTINGS_MODULE``),
installs all project dependencies, updates pip, migrates the database, and starts the Django server
with gunicorn.

**Usage:** Ensures consistent dependency management and environment setup on Windows systems,
optimizing the development workflow and maintaining project integrity across different platforms.

3.3) or create your own virtual environment and use: ::

$ make setup_install

Description: This command sets up the local environment variables (``DJANGO_SETTINGS_MODULE``) and
then installs all project dependencies, updates pip, migrates the database using
``python manage.py migrate``, and starts the Django server with gunicorn.

Usage: It combines the functionalities of setting up environment variables and installing
dependencies, crucial for initializing the Django application in various environments.

**4) Run the server**

1. ``$ python manage.py runserver``
2. ``$ gunicorn oc_lettings_site.wsgi:application``

and navigate to http://127.0.0.1:8000 in your browser
