# pull official base image
FROM python:3.9.19-slim

# set work directory
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY fp$9^593hsriajg$_%9g!1qa@ew(o-1#@=&4%=hp46(s

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input

# start Django application
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "oc_lettings_site.wsgi:application" ]
