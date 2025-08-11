from .base import *
# DEBUG = False 가 배포 환경,  EC2 에서 개발 환경으로 True 설정
DEBUG = False

#ALLOWED_HOSTS = ['3.25.53.53',]
ALLOWED_HOSTS = ['aimsmanu.com', 'www.aimsmanu.com',
                 '127.0.0.1', 'localhost',
                '3.25.53.53'  # runserver로 IP로 테스트할 때 필요
                 ]

# HTTPS 리버스프록시(Nginx) 사용 시 필수
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CSRF: HTTPS 도메인 신뢰 추가
CSRF_TRUSTED_ORIGINS = [
    'https://aimsmanu.com',
    'https://www.aimsmanu.com',
]
# (IP로 http 테스트한다면 임시로)
# CSRF_TRUSTED_ORIGINS += ['http://YOUR.EC2.PUBLIC.IP']


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