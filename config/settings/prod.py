from .base import *
# DEBUG = False 가 배포 환경,  EC2 에서 개발 환경으로 True 설정
DEBUG = False

ALLOWED_HOSTS = ["aimsmanu.com", "www.aimsmanu.com"]

# HTTPS 리버스프록시(Nginx) 사용 시 필수
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# CSRF: HTTPS 도메인 신뢰 추가
CSRF_TRUSTED_ORIGINS = [
    "https://aimsmanu.com",
    "https://www.aimsmanu.com",
]
# (IP로 http 테스트한다면 임시로)
# CSRF_TRUSTED_ORIGINS += ['http://YOUR.EC2.PUBLIC.IP']


MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware" ) # SecurityMiddleware 바로 다음
    
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"