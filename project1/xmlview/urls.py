from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('xmlview.views',
    url(r'^$', 'list'),
    url(r'^(?P<xml_id>\S+)/save$', 'save'),
    url(r'^(?P<xml_id>\S+)$', 'edit'),
)


