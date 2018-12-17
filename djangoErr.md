
# Error Case 
## DisallowedHost at /
add ALLOWED_HOSTS in settings.py 
ALLOWED_HOSTS = [ 
        '10.181.21.192',
]

## MySQLdb module error 
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?

(tutorial-env) [root@mrpdcnnetapp footprint]# sudo yum install MySQL-python

resolution: pip install mysqlclient 

# MakeMigrations and migrate
python manage.py makemigrations <app>: Create the migrations (generate the SQL commands).

python manage.py migrate: Run the migrations (execute the SQL commands).

(tutorial-env) [hpark84@mrpdcnnetapp footprint]$ python manage.py makemigrations mist
Migrations for 'mist':
  mist/migrations/0001_initial.py
    - Create model ArpTable


$ python manage.py migrate
table creation in database 
