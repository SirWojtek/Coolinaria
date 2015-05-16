from django.conf.urls import patterns, url
from ingredients import views

urlpatterns = patterns('',
    url(r'^$', views.ingredientIndex, name = 'ingredientIndex')
)