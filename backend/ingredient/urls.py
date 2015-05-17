from django.conf.urls import patterns, url
from ingredient import views

urlpatterns = patterns('',
    url(r'^$', views.ingredientIndex, name = 'ingredientIndex'),
    url(r'^topIngredients$', views.topIngredients, name = 'topIngredients'),
    url(r'^stats/display/all$', views.statsDisplayAll, name = 'statsDisplayAll'),
    url(r'^stats/display/(\d+)$', views.statsDisplay, name = 'statsDisplay')
)