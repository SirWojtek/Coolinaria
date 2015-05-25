from django.conf.urls import patterns, url
from recipe import views

urlpatterns = patterns('',
    url(r'^get/(?P<id>\d+)/$', views.getId, name = 'getId'),
    url(r'^(?P<recipeId>[\d]+)/$', views.update, name = 'update'),
    url(r'^new/$', views.create, name = 'create'),
    url(r'^remove/(?P<recipeId>[\d]+)/$', views.delete, name = 'delete'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^toaccept/$', views.toAccept, name = 'toAccept')
)
