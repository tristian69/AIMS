from django.urls import path
from . import views

app_name = 'newstech'

urlpatterns = [
    path('', views.newstech, name='newstech'),
]