# Orange County Lettings

## Description:
Project 13 OpenClassrooms Path - Orange Country Lettings -- 
Scale a Django application using a modular architecture 

For this last project of the OpenClassrooms Python Developer path, I undertook the task of 
refactoring a Django application to enhance its efficiency and maintainability. As part of this 
process, I meticulously crafted unit tests using Django's TestCases to ensure the reliability and 
integrity of the codebase. Additionally, I rigorously verified the codebase using flake8 to detect
and rectify any syntax errors or style violations, ensuring adherence to best practices.

To further fortify the project, I aimed for a minimum test coverage of 80%, employing tools such 
as coverage.py to gauge and improve the comprehensiveness of the tests.

After the successful refactoring, I encapsulated the Django application within a Docker image 
using a Dockerfile, facilitating consistent and reproducible deployment environments. This Docker 
image was subsequently hosted on Docker Hub for accessibility and distribution purposes.

To automate the deployment process, I implemented a GitHub Actions pipeline, configuring it to 
build, test, and deploy the project seamlessly. Leveraging the power of Render for deployment, 
I orchestrated the deployment pipeline to seamlessly transition the refactored Django application 
from development to production environments.

For deployment, I employed Gunicorn as the HTTP server and Whitenoise for serving static files, 
ensuring efficient and secure deployment of the Django application. This holistic approach to 
project management and deployment has not only optimized the performance and reliability of the 
Django application but also streamlined the deployment process for future iterations. My last 
step was to document my project with Read the Docs and Sphinx.

---
## Documentation
You can find a detailed documentation for the Django project of Orange Country Lettings 
on [Read-the-Docs](https://orange-country-lettings.readthedocs.io/en/latest/) 

---
## Deployed on Render
This project has been successfully deployed on [Render](https://render.com/)! Render is a cloud 
platform that makes it easy to deploy and manage applications, ensuring that our project is 
scalable, reliable, and accessible from anywhere. 
You can access our live project deployment on Render using the following link:

[Orange Country Lettings-Project URL](https://oc-lettings-site-latest-c1cc.onrender.com)

Feel free to explore the application, and don't hesitate to provide feedback or report any 
issues you encounter.

---
## Installation
### Possibility 1: Retrieving the Latest Docker Image


*Ensure you have your Docker Hub login credentials ready.*

Login to Docker Hub and pull the Latest Docker Image:

`$ make pull_docker_image_python`

Verify the Pulled Image and get the ``TAG``:

`$ docker images`

Run the Docker Container:

`$ make run_docker_image`

### Possibility 2: Clone the GitHub repository

**1) Clone the GitHub repository**

`$ git clone https://github.com/DoriDoro/OC_lettings.git` <br>
`$ cd OC_lettings`


**2) Create a SECRET_KEY**

create a `SECRET_KEY` with command:

`$ make generate_secret_key`

and replace the ``SECRET_KEY`` in file: oc_lettings_site/settings-local-template


**3) Install all dependencies**

choose a simple setup including creating a virtual environment, set up the
`DJANGO_SETTINGS_MODULE` in terminal and install all dependencies:

**3.1) for Linux/Mac:**

`$ make virtual_linux_setup_install`

**Description:** This command is tailored for Linux and macOS environments. It first sets up a
virtual environment to isolate Python dependencies, then configures the local environment variables
(``DJANGO_SETTINGS_MODULE``), and finally installs all project dependencies, updates pip,
migrates the database, and starts the Django server with gunicorn.

**Usage:** Ideal for ensuring a clean and isolated development environment on Linux and macOS
systems, enhancing dependency management and consistency across different setups.

**3.2) for Windows:**

`$ make virtual_windows_setup_install`

**Description:** Designed for Windows environments, this command initiates a virtual environment to
isolate Python dependencies, sets up the local environment variables (``DJANGO_SETTINGS_MODULE``),
installs all project dependencies, updates pip, migrates the database, and starts the Django server
with gunicorn.

**Usage:** Ensures consistent dependency management and environment setup on Windows systems,
optimizing the development workflow and maintaining project integrity across different platforms.

**3.3) or create your own virtual environment and use:**

`$ make setup_install`

Description: This command sets up the local environment variables (`DJANGO_SETTINGS_MODULE`) and
then installs all project dependencies, updates pip, migrates the database using
`python manage.py migrate`, and starts the Django server with gunicorn.

Usage: It combines the functionalities of setting up environment variables and installing
dependencies, crucial for initializing the Django application in various environments.

**4) Run the server**

4.1 `$ python manage.py runserver` or <br>
4.2 `$ gunicorn oc_lettings_site.wsgi:application`

and navigate to http://127.0.0.1:8000 in your browser

**5) Admin panel**

- navigate to `http://localhost:8000/admin`
- use the login details: username: `admin`and password: `Abc1234!`
