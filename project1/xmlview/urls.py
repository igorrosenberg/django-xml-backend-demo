from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('xmlview.views',
    url(r'^$', 'list'),
    url(r'^create$', 'create'),
    url(r'^save/(?P<xml_id>\S+)$', 'save'),
    url(r'^edit/(?P<xml_id>\S+)$', 'edit'),
    url(r'^delete/(?P<xml_id>\S+)$', 'delete'),
)


