from django.conf.urls import url
from employee import views

urlpatterns = [
    url('weather', views.weather, name='weather'),
]
