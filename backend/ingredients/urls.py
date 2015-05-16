from django.conf.urls import patterns, url
from ingredients import views

urlpatterns = patterns('',
    url(r'^/new$', views.addIngredient, name = 'addIngredient'),
    url(r'^/edit$', views.editIngredient, name = 'editIngredient'),
    url(r'^/delete$', views.deleteIngredient, name = 'deleteIngredient'),
    url(r'^$', views.getIngredients, name = 'getIngredients')
)