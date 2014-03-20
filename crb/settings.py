import os, sys
import localsettings
DEBUG = localsettings.DEBUG
TEMPLATE_DEBUG = DEBUG

from manage import PROJECT_DIR

ADMINS = (
    ('Kowit C.', 'kowit.s.c@gmail.com'),
)

MANAGERS = ADMINS
DATABASES = localsettings.DATABASES
TIME_ZONE = 'Asia/Bangkok'
LANGUAGE_CODE = 'th'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = PROJECT_DIR+'/crb/media/',
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR+'/crb/static_root/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR+'/crb/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
GRAPPELLI_INDEX_DASHBOARD = 'crb.dashboard.CustomIndexDashboard'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '*=g&amp;qyy+yl*fnz(a+sar67-#05-0)@9d_tmquy&amp;aiitdf@tdg&amp;'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
                               'django.core.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.core.context_processors.debug',
                               'django.core.context_processors.i18n',
                               'django.core.context_processors.media',
                               'django.core.context_processors.static',
                               'django.core.context_processors.csrf'
)

ROOT_URLCONF = 'crb.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crb.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR+'/crb/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    # South DB Migrate tools
    'south',
    'debug_toolbar',
    'pagination',

    #'gunicorn',

    #User app
    'holiday',
    'room',
    'staff',
    'academic',
    'activity',
    'transaction_log',
    'report',
)
FIRSTWEEKDAY = 6

#Debug toolsbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    }

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
