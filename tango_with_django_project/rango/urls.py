# New urls for our app

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^index/', views.index, name='index'), #Index
    url(r'^about/', views.about, name='about'), # About
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', #Category
        views.show_category, name='show_category'),
]
