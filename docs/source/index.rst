=================================================
Welcome to Orange Country Lettings documentation!
=================================================

**Orange County Lettings** is a pioneering startup within the property rental sector,
currently embarking on an expansion journey across the United States. This venture is part of a
broader trend in the real estate industry, where startups are leveraging technology and innovative
business models to disrupt traditional property management practices.


Pre-requirements
----------------

To be able to clone the Orange County Lettings GitHub repository and run this Django project from
GitHub, you'll need `Python <https://www.python.org/>`_,
`pip <https://pip.pypa.io/en/stable/installation/>`_, and
`Docker <https://docs.docker.com/engine/install/>`_ installed on your machine. Python and pip are
essential for managing the project's dependencies and running the Django server. Docker is
recommended for creating a consistent environment for the project, ensuring it runs smoothly
regardless of the host machine's configuration. Additionally, having
`Git <https://git-scm.com/downloads>`_ installed is crucial for cloning the repository from GitHub.


Clone GitHub repository
-----------------------

.. code-block:: console

   $ pip clone https://github.com/DoriDoro/OC_lettings.git
   $ cd OC_lettings


Generate a SECRET_KEY
---------------------

.. code-block:: console

   $ make generate_secret_key

copy the SECRET_KEY and add it inside the file: ``oc_lettings_site/settings-local-template``


Installation with IDE, virtual environment created
--------------------------------------------------

.. code-block:: console

   $ make setup_install


Installation Linux
------------------

.. code-block:: console

   $ make virtual_linux_setup_install


Installation Windows
--------------------

.. code-block:: console

   $ make virtual_windows_setup_install


Installation classic
--------------------

**1.** create a virtual environment

.. code-block:: console

   $ python3 -m venv venv
   $ . venv/bin/activate on MacOS and Linux
   $ venv\Scripts\activate on Windows

**2.** create a virtual environment

.. code-block:: console

   (venv) $ pip install --requirement requirements.txt

**3.** create a local settings file

Use the ``settings-local-template.py`` file which is located in
``oc_lettings_site/settings-local-template.py`` to set your local settings. Create a SECRET_KEY and
set the SENTRY_DSN.

**4.** set the environment variable

**4.1** in PyCharm:

go to ``File > Settings > Tools > Terminal`` and enter in field: ``Environment variables:``
this line: ``DJANGO_SETTINGS_MODULE=oc_lettings_site.settings-local-template``

.. note::

    close all open Terminals and reopen them otherwise the environment variable will not be set.

**4.2** in a terminal:

.. code-block:: console

   (venv) $ export SECRET_KEY=enter_your_secret_key
   (venv) $ export SENTRY_DSN=enter_your_sentry_dsn

**5.** run the server

**5.1** classic

.. code-block:: console

   (venv) $ python manage.py runserver

**5.2** with gunicorn

or use gunicorn

.. code-block:: console

   (venv) $ gunicorn oc_lettings_site.wsgi:application

