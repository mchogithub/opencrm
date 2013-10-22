from django.conf.urls import patterns, include, url
from opencrm import views
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'opencrm.views.home', name='home'),
	# url(r'^opencrm/', include('opencrm.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	(r'^accounts/', include('allauth.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^accounts/profile/$', include(admin.site.urls)),
	(r'^avatar/', include('avatar.urls')),


	#OpenCRM front-end
#	url(r'^opencrm/', include('opencrm.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)