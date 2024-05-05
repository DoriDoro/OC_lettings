# pull official base image
FROM python:3.9.19-slim

# set work directory
WORKDIR /oc_lettings

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /oc_lettings
RUN pip install -r requirements.txt

# copy project
COPY . /oc_lettings

# Collect static files
RUN python manage.py collectstatic --no-input

# start Django application
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "oc_lettings_site.wsgi:application" ]
