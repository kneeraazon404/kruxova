from core.settings.base import *

# Production environment overrides (PostgreSQL)
DEBUG = False

# Adjust to your actual production hosts
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'INFO',
        # },
    }
}
