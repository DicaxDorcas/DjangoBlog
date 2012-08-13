from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dblog.views.index'),
    url(r'^(?P<article_id>\d+)/$', 'dblog.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)
