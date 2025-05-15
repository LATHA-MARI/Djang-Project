import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['your-deployment-domain.com', 'localhost']
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}
