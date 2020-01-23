# django-mini-test-project


django 

1. start env

source python-3-env/bin/activate

source ../../python-projects/python-3-env/bin/activate

cd ../../python-projects/django-projects/project01

2. start server

python manage.py runserver 0.0.0.0:7070

python manage.py createsuperuser

user: george
pasword: lungu100
email test@test.ro


3.  models migrate comands

a. make oine it dose not exists

pmanage.py makemigrations webapp

b. migrate it

pmanage.py migrate webapp
