# pull official base image
FROM python:3.9.19-slim

# set work directory
WORKDIR /oc_lettings

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# settings-local.py stores all sensitiv data to run the django app
#ENV DJANGO_SETTINGS_MODULE oc_lettings_site.settings-local
ENV SECRET_KEY 'fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s'
ENV ALLOWED_HOSTS localhost 127.0.0.0.1
ENV DEBUG False
ENV NAME 'oc-lettings-site.sqlite3'
ENV SENTRY_DSN https://2c2fc0c6f3e6a397eea86b00e4bdb02b@o4506774266249216.ingest.us.sentry.io/4506925861502976

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

## start Django application
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
