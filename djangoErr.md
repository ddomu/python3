
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

