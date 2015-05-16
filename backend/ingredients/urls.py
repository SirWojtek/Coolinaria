from django.conf.urls import patterns, url
from ingredients import views

urlpatterns = patterns('',
    url(r'^/$', views.getIngredients, name = 'getIngredients'),
    url(r'^/new$', views.addIngredient, name = 'addIngredient')
)