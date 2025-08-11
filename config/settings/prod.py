from .base import *
# DEBUG = False 가 배포 환경,  EC2 에서 개발 환경으로 True 설정
DEBUG = False

#ALLOWED_HOSTS = ['3.25.53.53',]
ALLOWED_HOSTS = ['aimsmanu.com', 'www.aimsmanu.com',]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Security 바로 뒤
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"