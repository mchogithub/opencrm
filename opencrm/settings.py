# Django settings for opencrm project.

# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'opencrm',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': 'postgres',
		'PASSWORD': 'postgres',
		'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '',                      # Set to empty string for default.
	}
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['sviluppo.nwgitalia.it']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it-it'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.FileSystemFinder',	
#	'django.contrib.staticfiles.finders.DefaultStorageFinder',
	'pipeline.finders.PipelineFinder',
#	'less.finders.LessFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ow!&jmoq#mro&86vzh6camy9tb@yro^4y)l8=1sa-!u%(%)dp_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.gzip.GZipMiddleware',
	'pipeline.middleware.MinifyHTMLMiddleware',    
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.doc.XViewMiddleware',
#	'cms.middleware.page.CurrentPageMiddleware',
#	'cms.middleware.user.CurrentUserMiddleware',
#	'cms.middleware.toolbar.ToolbarMiddleware',
#	'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'opencrm.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'opencrm.wsgi.application'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths
#	os.path.join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'grappelli',    
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	'south',
	'pipeline',
	'opencrm',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	# ... include the providers you want to enable:
#	'allauth.socialaccount.providers.bitly',
#	'allauth.socialaccount.providers.dropbox',
#	'allauth.socialaccount.providers.facebook',
#	'allauth.socialaccount.providers.github',
	'allauth.socialaccount.providers.google',
#	'allauth.socialaccount.providers.instagram',
#	'allauth.socialaccount.providers.linkedin',
#	'allauth.socialaccount.providers.openid',
#	'allauth.socialaccount.providers.persona',
#	'allauth.socialaccount.providers.soundcloud',
#	'allauth.socialaccount.providers.stackexchange',
#	'allauth.socialaccount.providers.twitch',
#	'allauth.socialaccount.providers.twitter',
#	'allauth.socialaccount.providers.vimeo',
#	'allauth.socialaccount.providers.vk',
#	'allauth.socialaccount.providers.weibo',
	'avatar',
#	'cms',
#	'mptt',
#	'menus',
#	'sekizai',
#	'cms.plugins.flash',
#	'cms.plugins.googlemap',
#	'cms.plugins.link',
#	'cms.plugins.snippet',
#	'cms.plugins.text',
#	'cms.plugins.twitter',
#	'cms.plugins.file',
#	'cms.plugins.picture',
#	'cms.plugins.teaser',
#	'cms.plugins.video', 
#	'filer',
#	'cmsplugin_filer_file',
#	'cmsplugin_filer_folder',
#	'cmsplugin_filer_image',
#	'cmsplugin_filer_teaser',
#	'cmsplugin_filer_video',
#	'reversion',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

#PIPELINE_ENABLED = ('True')

PIPELINE_COMPILERS = (                          # used for compiling LESS files 
		'pipeline.compilers.less.LessCompiler',
	)

PIPELINE_LESS_BINARY = (
		'/usr/local/bin/lessc'
	)

PIPELINE_YUGLIFY_BINARY = (
	'/usr/local/bin/yuglify'
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.request",
	"allauth.account.context_processors.account",
	"allauth.socialaccount.context_processors.socialaccount",
#	'django.core.context_processors.i18n',
#	'django.core.context_processors.media',
#	'django.core.context_processors.static',
#	'cms.context_processors.media',
#	'sekizai.context_processors.sekizai',
)

AUTHENTICATION_BACKENDS = (
	# Needed to login by username in Django admin, regardless of `allauth`
	"django.contrib.auth.backends.ModelBackend",

	# `allauth` specific authentication methods, such as login by e-mail
	"allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = {
	'google': {
		'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
		  'AUTH_PARAMS': { 'access_type': 'online' }
	}
}

SOCIALACCOUNT_AVATAR_SUPPORT = 'avatars'

#AVATAR_RESIZE_METHOD = 'Image.BILINEAR'

AUTO_GENERATE_AVATAR_SIZES = (30,)

GRAPPELLI_ADMIN_TITLE = 'OpenCRM'