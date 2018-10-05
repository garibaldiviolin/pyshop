# PyShop

PyShop is a e-commerce website and REST API made in Python language, using Django and Django REST Framework.


## Overview

PyShop website allows customers to search and buy products online, track progress and understand details of their orders.
The platform also allows the managers to use the RESTAPI or a private section of the website (manually) to control the e-commerce data.
As said above, the application was built in Python, using Django, Django REST Framework, and uses coverage to analyze how much code is covered by the unit tests (apps' tests directory).


## Software Requirements

- [python 3.5+](https://www.python.org/)
- [Django 2.0+](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.8+](http://www.django-rest-framework.org/#installation)
- [Coverage.py 4.3+](https://coverage.readthedocs.io/en/coverage-4.5.1a/install.html)

Although it is not necessary, it is highly recommended to use  [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) in the steps below, since it isolates the project's environment, allowing the development of many different projects' versions with different dependencies' versions.

### Installing Dependencies

```bash
# After navigating to the project pyshop/src directory, install virtualenvwrapper
$ pip install virtualenvwrapper
# Additional steps (only for Linux users)
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
# Create isolated enviroment (using "pyshop" as the name for the environment)
$ mkvirtualenv pyshop
# Use the pyshop environment created
$ workon pyshop
# Install the requirements
$ pip install -r requirements.txt
```


### Running the Project

```bash
# Use the pyshop environment
$ workon pyshop
# After navigating to the project pyshop/src directory, execute migrations
$ python manage.py migrate
# Start the server
$ python manage.py runserver

```


### API Documentation

https://garibaldiviolin.github.io/pyshop/


### Inserting sample data for tests

It is available in the project's directory a sample data to be used to manually test the website (via browser) and the REST API:

```bash
# Use the pyshop environment
$ workon pyshop
# After navigating to the project pyshop/src directory, execute migrations
$ python manage.py migrate
# Load the sample data
$ python manage.py loaddata sample_data.json
# Start the server
$ python manage.py runserver
```


### Logging

PyShop uses python built-in logging library to trace and analyze incoming requests. By default, the log is disabled. To enable information logging, the application expects a configuration file (logging.conf) and the "logs" folder in the same directory as manage.py.
There is a configuration file example (logging.conf_file) available in the project. Just rename this file to logging.conf, create the logs directory, restart the web server (python manage.py runserver), and a file will be created in the logs folder. The information level in this log depends on the configuration set in logging.conf.


### Development Environment

- Python 3.5.2
- Django 2.0.7
- Django Rest Framewok 3.8.2
- Coverage.py 4.5.1
- Sublime Text 3.1.1 with Anaconda (Python package)
- Xubuntu GNU/Linux Operating System (16.04.5 LTS version)
- SQLite DBMS (for production use, MySQL or PostgreSQL is recommended instead)


### Running django unit tests

```bash
# After navigating to the project pyshop/src directory, execute tests
$ coverage run --source ./ ./manage.py test manager website -v 2
```

- The command above uses coverage.py library to analyze how much code the tests executed can cover. If the tests were executed with no errors, then the command shell should show the following messages in the last lines shown in the terminal (the time period may have a different value on a different machine, and number of tests - "nn" in the following lines - may change depending on the application's version):

```bash
Ran nn tests in 0.455s

OK
Destroying test database for alias 'default'
```

- To analyse how much these tests cover each python script from this project, execute the following command:

```bash
# Show each python script of the project and how much code is covered with the tests
$ coverage report
```
