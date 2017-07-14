from django.conf.urls import include, url
from . import views

urlpatterns = [ # Home page
        url(r'^$', views.index, name='index'),
        ]
