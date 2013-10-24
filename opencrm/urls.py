from django.conf.urls import patterns, include, url
from opencrm import views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'opencrm.views.home', name='home'),
	# url(r'^opencrm/', include('opencrm.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	(r'^accounts/', include('allauth.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^accounts/profile/$', include(admin.site.urls)),
	(r'^avatar/', include('avatar.urls')),

	#OpenCRM front-end
#	url(r'^opencrm/', include('opencrm.urls')),
)

"""urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns"""
