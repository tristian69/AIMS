from .base import *
# DEBUG = False 가 배포 환경,  EC2 에서 개발 환경으로 True 설정
DEBUG = False

ALLOWED_HOSTS = ['3.25.53.53',]

STATIC_URL = '/static/'

STATIC_ROOT = [BASE_DIR / 'static']