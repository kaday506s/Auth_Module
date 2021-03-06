"""
Django settings_old for config project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings_old and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta
from configurations import Configuration
from decouple import config


class Base(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Quick-start development settings_old - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config('SECRET_KEY', cast=str)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'corsheaders',
        'apps.authorization',
        'rest_framework',
        'rest_framework.authtoken',
        'drf_yasg'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.RemoteUserMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'config.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.'
                    'UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.'
                    'MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.'
                    'CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.'
                    'NumericPasswordValidator',
        },
    ]

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
    }

    # SWAGGER SETTINGS
    SWAGGER_SETTINGS = {
        'USE_SESSION_AUTH': False,
    }

    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/
    LANGUAGES = (
        ('en-us', 'English'),
        ('uk-ukr', 'Ukranian'),
    )

    LANGUAGE_CODE = 'uk-ukr' 'en-us'

    TIME_ZONE = 'Europe/Kiev'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    LOGIN_REDIRECT_URL = '/'

    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
    )

    CORS_ALLOW_CREDENTIALS = True

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': False,
        'BLACKLIST_AFTER_ROTATION': True,

        'ALGORITHM': 'HS256',
        'SIGNING_KEY': SECRET_KEY,
        'VERIFYING_KEY': None,
        'AUDIENCE': None,
        'ISSUER': 'authp',

        'AUTH_HEADER_TYPES': ('Bearer',),
        'USER_ID_FIELD': 'id',
        'USER_ID_CLAIM': 'user_id',

        'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
        'TOKEN_TYPE_CLAIM': 'token_type',

        'JTI_CLAIM': 'jti',

        'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
        'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
        'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    }


class DevLocal(Base):
    DEBUG = config('DEBUG', cast=bool)

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', cast=str),
            'USER': config('DB_USER', cast=str),
            'PASSWORD': config('DB_PASSWORD', cast=str),
            'HOST': config('DB_HOST', cast=str),
            'PORT': config('DB_PORT', cast=int),
        }
    }

    CORS_ORIGIN_ALLOW_ALL = True
    CURRENT_HOST = 'http://localhost:8000'


