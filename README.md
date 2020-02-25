# django-mini-test-project

0. Min. Requirements:

    - python version 3.6.9

    - django 2.0.5

1. first create a virtual envirement for python django, here is a good ex. how:

        https://tutorial.djangogirls.org/en/django_installation/

2. Download this project and all content place it in project file.

3. Start the envirement in a terminal ex. comand (this is for ubuntu):

    - To activate envirement:
  
        Path to the envirement:
      
          source YOUR_PATH_ENV_FOLDER/python-3-env/bin/activate
    
        Mine is:
      
          source ../../python-projects/python-3-env/bin/activate
    
    - open project folder in terminal:
  
          cd YOUR_PATH_ENV_PROJECTS_FOLDER/project01 
    
        Mine is:
      
          cd ../../python-projects/django-projects/project01

4. If all is good start the server with comand:
    
   python manage.py runserver 0.0.0.0:7070
  
    - Note. I am runing this server on localhost port 7070, change the host (if needed) in:
  
            https://github.com/LunguGeorgeProgramator/django-mini-test-project/blob/master/mainApp/settings.py
    
            ALLOWED_HOSTS = ['0.0.0.0', 'localhost']
    
    - I am using port 7070 just because it is free on my machine, can be set any be changing the comand from point 4. above.
    - The site can be viewed in a browser by loading one of the links:
      - http://localhost:7070/
      - http://0.0.0.0:7070/

5. (optional) if needed admin is active just a user needs to be created with comand:

     python manage.py createsuperuser
    
     - Link for admin is:
      
            http://0.0.0.0:7070/admin/

6. (optional) if migration is neede just run comand:

        python manage.py migrate

7. To run tests files, just run comand:

        ./manage.py test
