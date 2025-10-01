from .base import *
# DEBUG = False 가 배포 환경,  EC2 에서 개발 환경으로 True 설정
DEBUG = False

ALLOWED_HOSTS = [
    "13.210.142.129",
    "aimsmanu.com",
    "www.aimsmanu.com",
    "api.aimsmanu.com",
]

# HTTPS 리버스프록시(Nginx) 사용 시 필수
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# CSRF: HTTPS 도메인 신뢰 추가
CSRF_TRUSTED_ORIGINS = [
    "https://aimsmanu.com",
    "https://www.aimsmanu.com",
    "https://api.aimsmanu.com",
    # "http://13.210.142.129",  # runserver/비SSL 테스트 때만 일시적으로 사용
]
# (IP로 http 테스트한다면 임시로)
# CSRF_TRUSTED_ORIGINS += ['http://YOUR.EC2.PUBLIC.IP']
# base.py에서 CORS_ALLOW_ALL_ORIGINS=True라면, 배포에선 좁히는 걸 권장
# 예: (필요 시)
# CORS_ALLOW_ALL_ORIGINS = False
# CORS_ALLOWED_ORIGINS = [
#     "https://aimsmanu.com",
#     "https://www.aimsmanu.com",
#     "https://api.aimsmanu.com",
# ]

# --- 보안(HTTPS 전제) ---
SECURE_SSL_REDIRECT = True                # 항상 HTTPS로 리다이렉트 (Nginx가 X-Forwarded-Proto 설정해야 함)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS는 모든 트래픽이 HTTPS로 안정화된 뒤에만 켜세요.
SECURE_HSTS_SECONDS = 31536000            # 1년
SECURE_HSTS_INCLUDE_SUBDOMAINS = True     # 서브도메인 포함
SECURE_HSTS_PRELOAD = True                # Chrome preload 목록 등록 고려 시

# --- Static files ---
# WhiteNoise 사용: SecurityMiddleware 바로 다음에 살려두세요.
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# WhiteNoise 압축+해시 스토리지 (collectstatic 필수)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# base.py의 STATIC_URL/STATIC_ROOT/STATICFILES_DIRS 그대로 상속 사용
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "static"]

# --- 로깅(선택, 에러만 표준 출력) ---
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}