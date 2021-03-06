"""
Django settings for lua project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import re
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'This is a default value')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == 'True'

ALLOWED_HOSTS = ["*"] if os.environ.get("LOCAL_MACHINE") else [".lualms.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Authentication
    # 'django_registration',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',

    # Cloud storage
    'storages',
    'cloudinary',

    # Polymorphic model types
    'polymorphic',

    # WYSIWYG Editor
    'ckeditor',

    # Support for nested inline models
    'nested_admin',

    # Custom permissions
    'guardian',
    'rolepermissions',

    # Django REST framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_httpsignature',
    'rest_framework_swagger',


    # Development/Debug
    # 'corsheaders',
    # 'livereload',
    'debug_toolbar',

    'lua.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Live debugging
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # Live reload
    # 'livereload.middleware.LiveReloadScript',

    # Cross-origin Resource Sharing
    # 'corsheaders.middleware.CorsMiddleware',

    # 2-Factor Authentication
    'django_otp.middleware.OTPMiddleware',

    # Twilio gateway
    'two_factor.middleware.threadlocals.ThreadLocals',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
]


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


# Authentication

OTP_TOTP_ISSUER = "Lua Learning Management System"

LOGIN_URL = 'two_factor:login'

# LOGIN_REDIRECT_URL = 'two_factor:profile'

TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'

TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_SID')

TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_TOKEN')

TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID')


# Permissions

ROLEPERMISSIONS_MODULE = 'lua.roles'

GUARDIAN_RAISE_403 = True


# For debugging
INTERNAL_IPS = '127.0.0.1'

ROOT_URLCONF = 'lua.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'lua/core/templates')
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

WSGI_APPLICATION = 'lua.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if os.environ.get("IN_DOCKER"):
    # Stuff for when running in Docker-compose.

    CELERY_BROKER_URL = 'redis://redis:6379/1'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/1'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "postgres",
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': "db",
            'PORT': 5432,
        }
    }
elif os.environ.get("DATABASE_URL"):
    # Stuff for when running in Dokku.

    # Parse the DATABASE_URL env var.
    USER, PASSWORD, HOST, PORT, NAME = re.match("^postgres://(?P<username>.*?)\:(?P<password>.*?)\@(?P<host>.*?)\:(?P<port>\d+)\/(?P<db>.*?)$", os.environ.get("DATABASE_URL", "")).groups()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': NAME,
            'USER': USER,
            'PASSWORD': PASSWORD,
            'HOST': HOST,
            'PORT': int(PORT),
        }
    }

    # CACHES = {
    #     "default": {
    #         "BACKEND": "django_redis.cache.RedisCache",
    #         "LOCATION": os.getenv("REDIS_URL", "") + "/1",
    #         "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    #     }
    # }

    SESSION_CACHE_ALIAS = "default"
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_COOKIE_AGE = 365 * 24 * 60 * 60
    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    CELERY_BROKER_URL = os.environ.get("REDIS_URL", "") + "/1"
    CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL", "") + "/1"

elif os.environ.get('LOCAL_MACHINE'):
    # Stuff for when running locally.

    CELERY_TASK_ALWAYS_EAGER = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'LUA_DB',
            'USER': 'csneto',
            'HOST': 'localhost',
            'PORT': '5432',
            'PASSWORD': 'someone better change this before it is too late',
        }
     }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database.sqlite3'
        }
    }

if os.getenv("EMAIL_HOST_PASSWORD", ""):
    # TODO: Change these to match email provider.
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    EMAIL_USE_TLS = True
    EMAIL_HOST = os.getenv('EMAIL_HOST', None)
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)
    EMAIL_PORT = 587
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SERVER_EMAIL = os.environ.get('SERVER_EMAIL')


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Moving static assets to DigitalOcean Spaces as per:
# https://www.digitalocean.com/community/tutorials/how-to-set-up-object-storage-with-django

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')

AWS_S3_ENDPOINT_URL = os.environ.get('AWS_ENDPOINT_URL')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_CUSTOM_DOMAIN')

AWS_LOCATION = os.environ.get('AWS_LOCATION')
AWS_STATIC_LOCATION = os.environ.get('AWS_STATIC_LOCATION')
AWS_PUBLIC_MEDIA_LOCATION = os.environ.get('AWS_MEDIA_LOCATION')
AWS_PRIVATE_MEDIA_LOCATION = os.environ.get('AWS_PRIVATE_MEDIA_LOCATION')

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=600',
}

AWS_IS_GZIPPED = True  # Default: False

# GZIP_CONTENT_TYPES = ''

MEDIA_ROOT = 'mediafiles/'

STATIC_ROOT = 'staticfiles/'

MEDIA_URL = '/media/'

STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_FILE_STORAGE = 'lua.storage_backends.MediaStorage'

STATICFILES_STORAGE = 'lua.storage_backends.StaticStorage'


# CKEditor configuration

# CKEDITOR_BASEPATH = f'static/'

CKEDITOR_UPLOAD_PATH = 'editor/'

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_RESTRICT_BY_DATE = True

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_THUMNAIL_SIZE = (48, 48)

CKEDITOR_FORCE_JPEG_COMPRESSION = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks', 'Preview']},
            {'name': 'about', 'items': ['About']},
            '/',
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}


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
    "DOC_EXPANSION": "None",
    "USE_SESSION_AUTH": True,

    "SHOW_REQUEST_HEADERS": True,
    "CUSTOM_HEADERS": {
      "Accept": "application/vnd.api+json",
      "Content-type": "application/vnd.api+json"
    },

    "ENCODING": "application/vnd.api+json",

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


# Error Logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

if os.environ.get("LOCAL_MACHINE") == 'True':
    from . import secrets
    ADMINS = secrets.ADMINS
else:
    ADMINS = [
        ('Lua LMS', 'bot@ekletik.com'),
    ]

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


if os.environ.get("DATABASE_URL"):
    # Advanced error reporting in production
    # Include settings when DOKKU environment is detected.

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://8f145b746aad495f99a9a7fbbc54765e@sentry.io/1447474",
        integrations=[DjangoIntegration()]
    )
