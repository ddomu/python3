
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


## Python3 error while setting up Venv 
    compilation terminated.
    error: command 'gcc' failed with exit status 1
    
    ----------------------------------------
Command "/home/DCNscriptman/mist_venv/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-ng6y1ea9/mysqlclient/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-eemb10sj/install-record.txt --single-version-externally-managed --compile --install-headers /home/DCNscriptman/mist_venv/include/site/python3.6/mysqlclient" failed with error code 1 in /tmp/pip-install-ng6y1ea9/mysqlclient/
(mist_venv) [DCNscriptman@mrpdna mist]$ pip install mysqlclient

#### RESOLUTION !!!! 
> [root@mrpdna ~]# yum install python36-devel
Loaded plugins: langpacks, product-id, rhnplugin, search-disabled-repos, subscription-manager
This system is receiving updates from RHN Classic or Red Hat Satellite.
Resolving Dependencies
--> Running transaction check
---> Package python36-devel.x86_64 0:3.6.6-1.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

