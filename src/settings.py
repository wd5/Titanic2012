# -*- coding: utf-8 -*-
# Django settings for perspectiva project.
import os

APPEND_SLASH = False

ADMINS = (('Glader', 'glader.ru@gmail.com'),)

MANAGERS = (('Shyti', 'linashyti@gmail.com'),)

SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'glader.ru@gmail.com'

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = 'core.Profile'

PROJECT_PATH = os.path.dirname(__file__)
FORCE_SCRIPT_NAME = ""

TIME_ZONE = 'Asia/Yekaterinburg'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = PROJECT_PATH + '/media/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin/media/'
DEBUG = False
TEMPLATE_DEBUG = DEBUG
IS_DEVEL = True
TIMING = False

SECRET_KEY = '12345'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
)

TEMPLATE_DIRS = ()

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'core.context.default',
    'messages.context_processors.inbox',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'core.middleware.Process404Middleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'pytils',
    'south',
    'core',
    'forum',
    'newspaper',
    'messages',
    'django.contrib.sites',
    'django.contrib.flatpages',
)

LOG_PATH = '/var/log/projects/titanic'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(name)-15s %(levelname)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter':'simple'
        },
        'file':{
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_PATH, 'traceback.log'),
            'formatter': 'verbose',
            },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'WARNING',
            'propagate': True,
            },
        }
}

try:
    from local_settings import *
except ImportError:
    pass
