from .base import *

# local settings
DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_URL = '/static/'
STATICFILES_DIRS = ((os.path.join(BASE_DIR, 'static')), )

