from django.conf.urls import patterns, include, url

from django.contrib import admin
from places.views import hello
from bank.views import home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^places/$', hello),
)
