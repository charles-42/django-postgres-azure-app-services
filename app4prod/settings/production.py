# settings/production.py
from .base import *


# Paramètres spécifiques à l'environnement de production

SECRET_KEY = "verysecret"

DJANGO_ENV = "production"

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres",
        'USER': "admin_charles",
        'PASSWORD': "secret1234&",
        'HOST': "djangoapppostgre.postgres.database.azure.com",
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
