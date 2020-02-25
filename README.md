# django-mini-test-project


django 

create a python env if needed with python version 3.6.9

1. start env

source python-3-env/bin/activate

source ../../python-projects/python-3-env/bin/activate

cd ../../python-projects/django-projects/project01

2. start server

python manage.py runserver 0.0.0.0:7070

http://0.0.0.0:7070/

python manage.py createsuperuser

http://0.0.0.0:7070/admin/

user: george
pasword: lungu100
email test@test.ro


3.  models migrate comands

a. make one if dose not exists

python manage.py makemigrations webapp

b. migrate it

python manage.py migrate webapp

Set a user for admin:

python manage.py createsuperuser

Ex:

user: george
pasword: lungu100
email test@test.ro

To run tests, comand:

./manage.py test
