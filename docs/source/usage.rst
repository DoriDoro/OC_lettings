Usage
=====

To be able to clone the Orange County Lettings GitHub repository and run this Django project from
GitHub, you'll need `Python <https://www.python.org/>`_,
`pip <https://pip.pypa.io/en/stable/installation/>`_, and
`Docker <https://docs.docker.com/engine/install/>`_ installed on your machine. Python and pip are
essential for managing the project's dependencies and running the Django server. Docker is
recommended for creating a consistent environment for the project, ensuring it runs smoothly
regardless of the host machine's configuration. Additionally, having
`Git <https://git-scm.com/downloads>`_ installed is crucial for cloning the repository from GitHub.


.. _installation:

Installation
------------
**First step:** clone the GitHub repository

.. code-block:: console

   $ pip clone https://github.com/DoriDoro/OC_lettings.git
   $ cd OC_lettings

**Second step:** create a virtual environment

.. code-block:: console

   $ python3 -m venv venv
   $ . venv/bin/activate on MacOS and Linux
   $ venv\Scripts\activate on Windows

**Third step:** create a virtual environment

.. code-block:: console

   (venv) $ pip install --requirement requirements.txt

**Forth step:** create a local settings file

Use the ``settings-local-template.py`` file which is located in
``oc_lettings_site/settings-local-template.py`` to set your local settings. Create a SECRET_KEY and
set the SENTRY_DSN.

**Fifth step:** set the environment variable

in PyCharm:

go to ``File > Settings > Tools > Terminal`` and enter in field: ``Environment variables:``
this line: ``DJANGO_SETTINGS_MODULE=oc_lettings_site.settings_local``

.. note::

    close all open Terminals and reopen them otherwise the environment variable will not be set.

in a terminal:

.. code-block:: console

   (venv) $ export SECRET_KEY=enter_your_secret_key
   (venv) $ export SENTRY_DSN=enter_your_sentry_dsn

**Sixth step:** run the server

.. code-block:: console

   (venv) $ python manage.py runserver

or use gunicorn

.. code-block:: console

   (venv) $ gunicorn oc_lettings_site.wsgi:application
