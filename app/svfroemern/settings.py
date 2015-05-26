"""
Django settings for svfroemern project.

For more information on this file, see
https://docs.djangoproject.com/en//topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en//ref/settings/
"""
import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
PROJECT_ROOT = dirname(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en//howto/deployment/checklist/

# Do not set SECRET_KEY or LDAP password or any other sensitive data here.
# Instead, create a local.py file on the server.


# can run in sqlite, no redis, no elasticsearch mode
# FULLSTACK enabled all the other shit

FULLSTACK = not not os.environ.get('SVFROEMERN_FULLSTACK')
if FULLSTACK:
    print('running FULLSTACK! Yeah!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


def custom_show_toolbar(request):
    return True
#    if request.user.is_superuser:
#        return True
#    return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'taggit',
    'modelcluster',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'debug_toolbar',
    'utils',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'svfroemern.urls'
WSGI_APPLICATION = 'svfroemern.wsgi.application'


DATABASES = dict(default=dict(ENGINE='django.db.backends.sqlite3', NAME='svfroemern.db'))

# Database
# https://docs.djangoproject.com/en//ref/settings/#databases
if FULLSTACK:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',  # Set to empty string for localhost.
            'PORT': '',  # Set to empty string for default.
            'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
        }
    }





# Internationalization
# https://docs.djangoproject.com/en//topics/i18n/

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True
FIRST_DAY_OF_WEEK=1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en//howto/static-files/

STATIC_ROOT = join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    join(DJANGO_ROOT, 'static'),
)

MEDIA_ROOT = join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'


# Django compressor settings
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


# Taggit 0.12 has moved its south migrations to separate folder
# http://django-taggit.readthedocs.org/en/latest/

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}


# Template configuration

from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)


# Use Redis as the cache backend for extra performance
if FULLSTACK:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': 'redis://redis/1',
            'KEY_PREFIX': 'svfroemern',
            'OPTIONS': {
                'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            }
        }
    }




# Wagtail settings

LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "svfroemern"

WAGTAILIMAGES_IMAGE_MODEL = "home.BetterImage"

# Use Elasticsearch as the search backend for extra performance and better search results
if FULLSTACK:
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
            'INDEX': 'svfroemern',
            'URLS': ['http://search:9200']
        },
    }

# Celery settings
# When you have multiple sites using the same Redis server,
# specify a different Redis DB. e.g. redis://localhost/5

BROKER_URL = 'redis://redis/2'

CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'NOTASECRET'


DATABASES['default']['PASSWORD'] = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Process all tasks synchronously.
# Helpful for local development and running tests
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True


if False: # production stuff

    # Do not set SECRET_KEY, Postgres or LDAP password or any other sensitive data here.
    # Instead, create a local.py file on the server.

    # Disable debug mode
    DEBUG = False
    TEMPLATE_DEBUG = False


    # Compress static files offline and minify CSS
    # http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
    COMPRESS_OFFLINE = True
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    ]


    # Configuration from environment variables
    # Alternatively, you can set these in a local.py file on the server

    env = os.environ.copy()

    # On Torchbox servers, many environment variables are prefixed with "CFG_"
    for key, value in os.environ.items():
        if key.startswith('CFG_'):
            env[key[4:]] = value


    # Basic configuration

    APP_NAME = env.get('APP_NAME', 'svfroemern')

    if 'SECRET_KEY' in env:
        SECRET_KEY = env['SECRET_KEY']

    if 'ALLOWED_HOSTS' in env:
        ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

    if 'PRIMARY_HOST' in env:
        BASE_URL = 'http://%s/' % env['PRIMARY_HOST']

    if 'SERVER_EMAIL' in env:
        SERVER_EMAIL = env['SERVER_EMAIL']


    # Database

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.get('PGDATABASE', APP_NAME),
            'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for

            # User, host and port can be configured by the PGUSER, PGHOST and
            # PGPORT environment variables (these get picked up by libpq).
        }
    }


    # Redis
    # Redis location can either be passed through with REDIS_HOST or REDIS_SOCKET

    if 'REDIS_HOST' in env:
        REDIS_LOCATION = env['REDIS_HOST']
        BROKER_URL = 'redis://%s' % env['REDIS_HOST']

    elif 'REDIS_SOCKET' in env:
        REDIS_LOCATION = 'unix://%s' % env['REDIS_SOCKET']
        BROKER_URL = 'redis+socket://%s' % env['REDIS_SOCKET']

    else:
        REDIS_LOCATION = None


    if REDIS_LOCATION is not None:
        CACHES = {
            'default': {
                'BACKEND': 'redis_cache.cache.RedisCache',
                'LOCATION': REDIS_LOCATION,
                'KEY_PREFIX': APP_NAME,
                'OPTIONS': {
                    'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
                }
            }
        }


    # Elasticsearch

    if 'ELASTICSEARCH_URL' in env:
        WAGTAILSEARCH_BACKENDS = {
            'default': {
                'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
                'URLS': [env['ELASTICSEARCH_URL']],
                'INDEX': APP_NAME,
            },
        }


    # Logging

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers':     ['mail_admins'],
                'level':        'ERROR',
                'propagate':    False,
            },
            'django.security': {
                'handlers':     ['mail_admins'],
                'level':        'ERROR',
                'propagate':    False,
            },
        },
    }


    # Log errors to file
    if 'ERROR_LOG' in env:
        LOGGING['handlers']['errors_file'] = {
            'level':        'ERROR',
            'class':        'logging.handlers.RotatingFileHandler',
            'filename':     env['ERROR_LOG'],
            'maxBytes':     5242880, # 5MB
            'backupCount':  5
        }
        LOGGING['loggers']['django.request']['handlers'].append('errors_file')
        LOGGING['loggers']['django.security']['handlers'].append('errors_file')


try:
    from .local import *
except ImportError:
    pass

