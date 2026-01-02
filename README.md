# review_django
---------------- EP -01--------------------
 #### Start a Django Project and file Structure 


>> pip install uv 
>> git init 
>> touch .gitignore
>> python3 -m venv myenv
>> source myenv/bin/activate
>> pip install django

>> django-admin startproject myproject
>> cd myproject
>> python3 manage.py runserver
>> python3 manage.py startapp myapp

**Exploration**
   1. manage.py --> command line utility to manage the django project.
   2. settings.py --> file that contains the settings and configuration for the django project.
   3. urls.py --> file that contains the url routing for the django project.
   4. views.py --> file that contains the view functions/controllers  for the django app.
   5. models.py --> file that contains the database models for the django app.
   6. admin.py --> file to register the models to the django admin panel.
   7. migrations/ --> folder that contains the database migration files for the django app.
   8. templates/ --> folder that contains the html files for the django app.
   9. static/ --> folder that contains the static files for the django app.   
   10. media/ --> folder that contains the media files uploaded by users. 
    11. you can make django views with the help of function based views or class based views.
    12. urls.py --> files in django decides which urls should be mapped which which view functions.

---------------- EP -02--------------------
#### Templates and Errors in Django


**Logical Structure :**

user -- request --> urls.py --> views.py --> templates/html files --- response --> user

1. create views.py  
2. Handles Urls in urls.py
3. Create templates folder in root app folder
4. Create static folder in root app folder
5. Configure settings.py for templates and static files.
6. templating Engine in django to render dynamic data in html files. 
 html file is works as template engine means you can inject dynamic data in html files using django template tags. 
    syntax --> {{ variable_name }}
7. {%load static%} --> to load static files in html files.
8. {% static 'path/to/static/file' %} --> to refer static files in html files.

