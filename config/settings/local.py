from .base import *

# local settings
DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]

