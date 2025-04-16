from core.settings.base import *

# Staging environment overrides (PostgreSQL)
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        # },
    }
}
