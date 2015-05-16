from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^backend/account/', include('account.urls', namespace = 'account')),
    url(r'^backend/recipe/', include('recipe.urls', namespace = 'recipe')),
    url(r'^backend/ingredients/', include('ingredients.urls', namespace = 'ingredients')),
    url(r'^backend/admin/', include(admin.site.urls)),
)
