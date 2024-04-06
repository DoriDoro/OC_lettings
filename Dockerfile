# pull official base image
FROM python:3.9.19

# set work directory
WORKDIR /Desktop/DR_P13/P13/oc_lettings

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# start Django application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
