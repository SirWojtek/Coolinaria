from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^account/', include('account.urls', namespace = 'account')),
    url(r'^recipe/', include('recipe.urls', namespace = 'recipe')),
    url(r'^ingredient/', include('ingredient.urls', namespace = 'ingredient')),
    url(r'^admin/', include(admin.site.urls)),
)
