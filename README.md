# SEPO
POSTECH Object Oriented Programming project6:SEPO

## to install and run SEPO 

1. Install Django
'pip3 install django'  

2. Install django-ckeditor
'pip3 install --user django-ckeditor'  

3. Install MySql on linux
'sudo apt-get install mysql-server'  
'sudo apt-get install libmysqlclient-dev'  
'pip install --user mysqlclient'  

6. DB settings
in sepo_server/settings.py, set DATABSES information with your MySql settings

7. in MySQL,
'CREATE DATABASE sepo6team;'

8. In terminal, execute the following queries.
python3 manage.py makemigrations  
python3 manage.py migrate  
python3 manage.py createsuperuser  

9. Run!
python3 manage.py runserver  


## Software Version

V 1.0  
initial version <django version 1.1>  

v 2.0  
updated by Jinho Ko  
updated to <django version 2.1.2>  
models.ForeignKey() positional requirements 'on-delete' addition -> on_delete=models.DO_NOTHING  
django.conf.urls.url : url(r'^admin/', admin.site.urls),  
django.contrib.auth : views.logout -> views.LogoutView  
some testfiles deleted
hyperlink among pages availability problem solved (from absolute address to relative address)


End.
