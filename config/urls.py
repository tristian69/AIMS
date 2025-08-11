from django.conf import settings  # settings 누락되지 않게 확인
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index, about
from users.views import signup
from users.forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  
    #path('', include('aims.urls')),  
    path('users/', include('users.urls', namespace='users')),
    path('dashboard/', include('dashboard.urls')),
    path('core/', include('core.urls')),      # core 앱과 연결
    path('about/', about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm ), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout 등 자동 제공
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)