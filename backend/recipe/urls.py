from django.conf.urls import patterns, url
from recipe import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name = 'index')
)