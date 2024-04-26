# pull official base image
FROM python:3.9.19-slim

# set work directory
WORKDIR /oc_lettings

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# settings-local.py stores all sensitiv data to run the django app
#ENV DJANGO_SETTINGS_MODULE oc_lettings_site.settings-local
ENV SECRET_KEY ${{ secrets.SECRET_KEY }}
ENV ALLOWED_HOSTS ${{ secrets.ALLOWED_HOSTS }}
ENV DEBUG ${{ secrets.DEBUG }}
ENV NAME ${{ secrets.DB_NAME }}
ENV SENTRY_DSN ${{ secrets.SENTRY_DSN }}

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

## start Django application
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
