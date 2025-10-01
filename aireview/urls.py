from django.urls import path
from . import views

app_name = 'aireview'

urlpatterns = [
    path('', views.aireview, name='aireview'),
]