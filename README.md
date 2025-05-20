# Basic-Task-List

This is a simple task list application built with Django. It allows users to add, update, and delete tasks.


## Features

- Add new tasks

- Update existing tasks

- Delete tasks

## Requirements

To run this project, you need to have the following installed on your machine:

- Django>=4.0
- selenium
- coverage
- webdriver-manager

(Note: You can install the requirements using pip install -r requirements.txt in the TaskList folder)

## Running the Project

1. Clone the repository

2. Install the requirements

3. Run the server

(Bash into TaskList folder) python manage.py runserver

4. Run the tests

(Bash into TaskList folder) 

'''bash
python manage.py test
'''

5. Run the coverage report

(Bash into TaskList folder) 

'''bash
coverage run manage.py test
coverage report
'''

### Coverage Report

Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
TaskListApp\__init__.py                          0      0   100%
TaskListApp\admin.py                             1      0   100%
TaskListApp\apps.py                              4      0   100%
TaskListApp\migrations\0001_initial.py           5      0   100%
TaskListApp\migrations\__init__.py               0      0   100%
TaskListApp\models.py                           11      1    91%
manage.py                                       11      2    82%
----------------------------------------------------------------
TOTAL                                          266      4    98%

## Docker

This project includes a Dockerfile to facilitate containerization. To build and run the Docker container, follow these steps:

1. Build the Docker image:

'''bash
docker-compose build
'''

2. Run the Docker container:

'''bash
docker-compose up
'''

## Testing Strategy

- Unit Tests: validate individual components (models).
- Integration Tests: verify interaction between views and models.
- E2E Tests: simulate user behavior using Selenium and Chrome.