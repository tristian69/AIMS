from .base import *

# local settings
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]

