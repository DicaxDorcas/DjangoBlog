from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^projects/$', 'project.views.index'),
    url(r'^projects/([-_A-Za-z0-9]+)/$', 'project.views.detail'),
    url(r'^$', 'dblog.views.index'), # To be removed.
    url(r'^blog/$', 'dblog.views.index'),
    url(r'^blog/([-_A-Za-z0-9]+)/$', 'dblog.views.detail'),
    url(r'^tags/$', 'dblog.views.tags'),
    url(r'^tag/([-_A-Za-z0-9]+)/$','dblog.views.with_tag'),
    url(r'^tag/([-_A-Za-z0-9]+)/page/(d+)/$', 'dblog.views.with_tag' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

