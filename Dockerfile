# pull official base image
FROM python:3.9.19

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# specific network port
EXPOSE 8000

# start Django application
CMD [ "python", "manage.py", "runserver" ]
