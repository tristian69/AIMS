from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env') if (BASE_DIR / '.env').exists() else None

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-2w#22$#d362x(@_ob=!9y$$4n7z241x-qq=2hdg@qi4xi0cf@r'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-secret')

#ALLOWED_HOSTS = ["13.210.142.129", "localhost", "127.0.0.1"]
#ALLOWED_HOSTS = ["api.aimsmanu.com"]
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aims',
    'core',
    'corsheaders', # 앱은 여기
    'users',
    'dashboard',
    'analytical',
    'rest_framework',
    'manuscripts',
    'aireview',
    'editor',
    'gallery',
    'publication',
    'newstech',
    'shopping',
    'members',
    'products',
]

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-XXXX-Y'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # (배포에서 Whitenoise 쓴다면 prod.py에서만 ↓ 추가)
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    # CORS는 CommonMiddleware 보다 앞!
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    
]

CSRF_TRUSTED_ORIGINS = [
    "http://13.210.142.129",
    "http://13.210.142.129:8000",   # runserver로 접근 시
    "https://aimsmanu.com",
    "https://www.aimsmanu.com",
    "https://api.aimsmanu.com",
    ]  # "https://your-domain.com",

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_ALL_ORIGINS = True

# REST Framework 기본 설정
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

#STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_DIRS = ((os.path.join(BASE_DIR, 'static')), )

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SILENCED_SYSTEM_CHECKS = ["rest_framework.W001"]