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

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

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



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not not os.environ.get('DJANGO_DEBUG', False)
TEMPLATE_DEBUG = DEBUG
if DEBUG:
    TEMPLATE_STRING_IF_INVALID = "!! FIXME: UNKNOWN !!"


DOMAIN="sv.froemern.de"

# we trust our environment
ALLOWED_HOSTS = ["*",]

if DEBUG and not os.environ.get('DJANGO_REAL_EMAIL'):
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = "SV Frömern Jugend (Webmaster) <webmaster@{}>".format(DOMAIN)

SERVER_EMAIL = "webserver@{}".format(DOMAIN)

ADMINS = (('Peter', 'pq@pqua.de'),)

#: Mailgun api key for using the REST API
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

#: Mailgun SMTP server host
MAILGUN_SMTP_SERVER = os.environ.get("MAILGUN_SMTP_SERVER")

#: Mailgun SMTP server login
MAILGUN_SMTP_LOGIN = os.environ.get("MAILGUN_SMTP_LOGIN")

#: Mailgun SMTP server password
MAILGUN_SMTP_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD")

#: Mailgun SMTP server port
MAILGUN_SMTP_PORT = int(os.environ.get("MAILGUN_SMTP_PORT", 0)) or None

if MAILGUN_SMTP_SERVER:

    #: Email host for sending mail
    EMAIL_HOST = MAILGUN_SMTP_SERVER

    #: Email server username
    EMAIL_HOST_USER = MAILGUN_SMTP_LOGIN

    #: Email server password
    EMAIL_HOST_PASSWORD = MAILGUN_SMTP_PASSWORD

    #: Email server SMTP port
    EMAIL_PORT = MAILGUN_SMTP_PORT




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
#    'debug_toolbar', # way to slow
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

STATIC_ROOT = join(PROJECT_ROOT, 'static_root')
STATIC_URL = '/static/'



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    join(DJANGO_ROOT, 'static'),
)

if os.path.exists('/Users/peter/'):
    MEDIA_ROOT = 'media/'
else:
    MEDIA_ROOT = '/app/media'

MEDIA_URL = '/media/'

SERVER_URL="sv.froemern.de"

AUTHENTICATION_BACKENDS = ('nopassword.backends.email.EmailBackend', 'django.contrib.auth.backends.ModelBackend')

NOPASSWORD_LOGIN_EMAIL_SUBJECT = 'Dein Login bei {}'.format(SERVER_URL)
NOPASSWORD_AUTOCOMPLETE = False
NOPASSWORD_LOGIN_CODE_TIMEOUT = 1800


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if os.environ.get('DATABASE_NAME'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DATABASE_NAME', 'postgres'),
            'USER': os.environ.get('DATABASE_NAME', 'postgres'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': 'postgres',
            'PORT': '',  # Set to empty string for default.
            'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
        }
    }



if 'REDIS_PORT' in os.environ:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': 'redis://redis:6379',
            'OPTIONS': {
                'DB': 13,
                'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            }
        }
    }

if 'ELASTICSEARCH_URL' in os.environ:
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
            'URLS': [os.environ['ELASTICSEARCH_URL']],
            'INDEX': 'wagtail',
            'TIMEOUT': 5,
        }
    }
else:
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.db.DBSearch',
        }
    }

CLOUDFLARE_EMAIL = os.environ.get('CLOUDFLARE_EMAIL')
CLOUDFLARE_TOKEN = os.environ.get('CLOUDFLARE_TOKEN')

if CLOUDFLARE_EMAIL:

    WAGTAILFRONTENDCACHE = {
        'cloudflare': {
            'BACKEND': 'wagtail.contrib.wagtailfrontendcache.backends.CloudflareBackend',
            'EMAIL': CLOUDFLARE_EMAIL,
            'TOKEN': CLOUDFLARE_TOKEN,
        },
    }


# Django compressor settings
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE=False
COMPRESS_CSS_HASHING_METHOD = 'hash'

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

# Wagtail settings

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "svfroemern"

WAGTAILSEARCH_RESULTS_TEMPLATE = 'home/search_results.html'

# Whether to use face/feature detection to improve image cropping - requires OpenCV
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False


WAGTAILIMAGES_IMAGE_MODEL = "home.BetterImage"


# Celery settings
# When you have multiple sites using the same Redis server,
# specify a different Redis DB. e.g. redis://localhost/5

BROKER_URL = 'redis://redis/7'

CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'Vicky und die starken Männer')



# Process all tasks synchronously.
# Helpful for local development and running tests
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
 'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'home': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
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




try:
    from .local import *
except ImportError:
    pass

