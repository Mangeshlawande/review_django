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