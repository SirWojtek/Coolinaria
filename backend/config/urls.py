from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'config.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^backend/recipe/', include('recipe.urls', namespace = 'recipe')),
    url(r'^backend/admin/', include(admin.site.urls)),
)
