from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from . import views

app_name = 'users'

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]