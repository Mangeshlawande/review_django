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

---------------- EP -03--------------------
#### Jinja2 and Django apps 
1. Jinja2 is a templating engine for python.
2. Django uses its own templating engine by default but you can also use Jinja2 with django.
3. To use Jinja2 with django you need to install Jinja2 package
   >> pip install Jinja2
4. Configure settings.py to use Jinja2 as templating engine.
5. Create a folder named 'jinja2' in your app folder to store jinja2 templates.
6. In settings.py add the following code to configure Jinja2 templating engine
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.jinja2.Jinja2',
           'DIRS': [os.path.join(BASE_DIR, 'your_app/jinja2')],
           'APP_DIRS': True,
           'OPTIONS': {
               'environment': 'your_app.jinja2.environment',
           },
       },
   ]
7. Create a file named 'jinja2.py' in your app folder to configure Jinja2 environment.
8. In jinja2.py add the following code
   from jinja2 import Environment, FileSystemLoader
   import os

   **createapp**
   >>python manage.py startapp your_app
   It gives some default files and folders to work with django.
   You can create multiple apps in a single django project for better code management.
   1.django only make this app not install it in project.
   2. to install app in project you need to add app name in settings.py file
   INSTALLED_APPS = [
       ...
       'your_app',
       ...
   ]
   
   in app make explicit urls.py
    from django.urls import path
    pass controller from main project urls.py to app urls.py


---------------- EP 04 --------------------

#### How to add tailwind in django and super user 
>> pip install 'django-tailwind[reload]'
add 'tailwind' in settings.py
>> python manage.py tailwind init
add theme in settings.py (INSTALLED_APPS)

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ["127.0.0.1"]
>> python manage.py tailwind install

**Run 1 more terminal to run tailwind css**
NPM_BIN_PATH=$(npm bin) \ (NO NEED TO GIVE )STANDALONE INSTALL 

>> python manage.py tailwind start
*In production*
>> python manage.py tailwind build

Hot reload accessible configuration 
add :++: Installed app :: 
django_browser_reload
>> pip install django_browser_reload
In settings.py add :++:
middleware :++: 'django_browser_reload.middleware.BrowserReloadMiddleware',
urls.py :++: path("__reload__/", include("django_browser_reload.urls")),

Django Admin panel: 
migrations talk with databases 
>> python manage.py migrate
after this you can access admin panel

Create superuser to access admin panel
>> python manage.py createsuperuser
provide username , email , password
Access admin panel at
>> localhost:8000/admin

---------------- EP 05 --------------------
#### Django Forms and Model Forms
1. Django forms are used to handle user input and validation.
2. Create a forms.py file in your app folder to define your forms.
3. In forms.py import forms from django
   from django import forms
4. Create a form class by inheriting from forms.Form or forms.ModelForm
5. Define form fields using form field classes like CharField, EmailField, etc.
6. In views.py import the form class and create an instance of the form.
7. Pass the form instance to the template context to render the form in html.
8. In the template use {{ form.as_p }} to render the form fields as paragraphs.
9. Handle form submission in views.py by checking if the request method is POST.
10. Validate the form using form.is_valid() method and process the form data.
11. For Model Forms, define a model in models.py and create a ModelForm class in forms.py
12. In the ModelForm class, define a Meta class to specify the model and fields to include.
13. Model Forms automatically handle saving data to the database when form.save() is called.
14. Use Model Forms in views.py similar to regular forms for rendering and processing user input.

reset django password
>> python manage.py changepassword username

for image config in settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    

add static and media in urls.py
from django.conf import settings
from django.conf.urls.static import static  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

>> python manage.py makemigrations
>> python manage.py migrate

add models in admin.py to see in admin panel
from .models import YourModel
admin.site.register(YourModel)

add 1 view to show data from model in views.py
