# pull official base image
# Use a specific version of the Python image optimized for Django
FROM python:3.9.19-slim

# Set a specific working directory
WORKDIR .

#Sset environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .
