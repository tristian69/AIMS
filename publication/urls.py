from django.urls import path
from . import views

app_name = 'publication'

urlpatterns = [
    path('', views.publication, name='publication'),
]