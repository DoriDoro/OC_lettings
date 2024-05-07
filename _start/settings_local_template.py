from oc_lettings_site.settings import *  # noqa

# create with these two lines in terminal a SECRET_KEY and put the created SECRET_KEY between ""
# python manage.py shell -c
# 'from django.core.management import utils; print(utils.get_random_secret_key())'
# SECRET_KEY = ""

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# create a Sentry project and add the SENTRY_DSN
# https://docs.sentry.io/platforms/python/integrations/django/
# SENTRY_DSN = ""
