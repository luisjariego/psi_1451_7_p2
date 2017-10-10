# New urls for our app

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^index/', views.index, name='index'), #Index
    url(r'^about/', views.about, name='about'), # About
	url(r'^add_category/$', views.add_category, name='add_category'), #Category (add)
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', #Category (show)
        views.show_category, name='show_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'), #Page (add)
]
