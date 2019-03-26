"""
Django settings for lua_server project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from datetime import timedelta
from . import secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # os.environ.get('DEBUG', False) == 'True'

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['.lualms.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'polymorphic',
    'cloudinary',
    'corsheaders',
    'livereload',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_httpsignature',
    'rest_framework_swagger',

    # 2-Factor Authentication
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',

    'lua_server.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Live reload
    'livereload.middleware.LiveReloadScript',

    # Cross-origin Resource Sharing
    'corsheaders.middleware.CorsMiddleware',

    # 2-Factor Authentication
    'django_otp.middleware.OTPMiddleware',

    # Twilio gateway
    'two_factor.middleware.threadlocals.ThreadLocals',
]

ROOT_URLCONF = 'lua_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'lua_server/core/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lua_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': secrets.DATABASES['postgres']['ENGINE'],
        'NAME': secrets.DATABASES['postgres']['NAME'],
        'USER': 'csneto', # secrets.DATABASES['postgres']['USER'],
        'HOST': 'localhost', # secrets.DATABASES['postgres']['HOST'],
        'PORT': secrets.DATABASES['postgres']['PORT'],
        'PASSWORD': secrets.DATABASES['postgres']['PASSWORD'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'core.User'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

if DEBUG:
    STATIC_ROOT = 'staticfiles'
    MEDIA_ROOT = 'mediafiles'
else:
    STATIC_ROOT = '/var/www/lualms/assets'
    MEDIA_ROOT = '/var/www/lualms/mediafiles'

# Cross-Origin Resource Sharing

CORS_ORIGIN_ALLOW_ALL = True

# REST FRAMEWORK

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,

    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',

    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),

    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',

    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',
        'rest_framework_json_api.filters.OrderingFilter',
        'rest_framework_json_api.django_filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),

    'SEARCH_PARAM': 'filter[search]',

    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),

    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}


JSON_API_FORMAT_FIELD_NAMES = 'dasherize'
JSON_API_FORMAT_TYPES = 'dasherize'
JSON_API_PLURALIZE_TYPES = False


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

SWAGGER_SETTINGS = {
    "LOGIN_URL": 'rest_framework:login',
    "LOGOUT_URL": 'rest_framework:logout',
    "APIS_SORTER": "alpha",
    "DOC_EXPANSION": "list",
    "USE_SESSION_AUTH": True,

    "SHOW_REQUEST_HEADERS": True,

    "JSON_EDITOR": True,
    "OPERATIONS_SORTER": 'method',
    "SECURITY_DEFINITIONS": {
        "api_key": {
            "type": "apiKey",
            "name": "Token ",
            "in": "header"
        }
    },
}

# 2-Factor Authentication
OTP_TOTP_ISSUER = "Lua Learning Management System"
LOGIN_URL = 'two_factor:login'
TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
# LOGOUT_URL = 'two_factor:logout'
# LOGIN_REDIRECT_URL = 'two_factor:profile' # optional
# TWO_FACTOR_QR_FACTORY = 'qrcode.image.pil.PilImage' # for PIL/Pillow
# PHONENUMBER_DEFAULT_REGION = # Default: None

TWILIO_ACCOUNT_SID = secrets.TWILIO['SID']
TWILIO_AUTH_TOKEN = secrets.TWILIO['TOKEN']
TWILIO_CALLER_ID = secrets.TWILIO['CALLER_ID']


# Error Logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

ADMINS = secrets.ADMINS

MANAGERS = ADMINS

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
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
