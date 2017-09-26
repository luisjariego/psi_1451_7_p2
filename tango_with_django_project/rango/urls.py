# New urls for our app

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #Index
    url(r'^index/', views.index, name='index'), #Index
    url(r'^about/', views.about, name='about'), # About
]
