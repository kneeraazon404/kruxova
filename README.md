# INSTALLATION

## ALLOWED_HOSTS

set the allowed host(ip-address no port)

`ALLOWED_HOSTS = ['*']`

#

## DATABASE CONFIGURATION

open the file 

**msdat_python_api_settings/settings_pro_pgsql.py**

this is the django_settings file for production enviroment using *POSTGRESQL database*

set the database values

- name - this this the name of the database
- user - an authorized user for the database
- password - the user password
- host - the database host-ip
- port- the host port

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "msdat-python-api",
        'USER': "e4emsdat",
        'PASSWORD':'e4emsdatdbpass',
        'HOST':'db',
        'PORT':'5432'
    }
}`

# 

## ENVIROMENT SETUP SCRIPTS

`bash script_bash_mark_as_staging.sh`

or

`bash script_bash_mark_as_production.sh`

# 

## LOADING INITIAL DATA

to load inital data from apps fixtures(NOTE:will override any existing data)

use only when needed to seed an empty db

`bash script_load_data.sh`

# 

## RUN

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

# 