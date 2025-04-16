from core.settings.base import *

# Local development with PostgreSQL (alternative to SQLite)
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'msdatoptimized',
        'USER': 'msdatoptimizeduser',
        'PASSWORD': '9mQ50sTO38l8',
        'HOST': 'localhost',
        'PORT': '',
    }
}
