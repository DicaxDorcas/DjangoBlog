from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dblog.views.index'),
    url(r'^(?P<article_id>\d+)/$', 'dblog.views.detail'),
    url(r'^/p/(?P<page_slug>\d+)/$', 'pages.views.page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
urlpatterns += staticfiles_urlpatterns()
