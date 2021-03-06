"""
Django settings for HanseiBox project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kqq9j8z@c%glyv4gtu%($_ig%2*2)$qxm*8w=cdp^v6y=pv53z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '_movie',
    '_user',
    '_seat',
    '_theater'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HanseiBox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/mnt/d/sjyoo/Study/DjangoMovie/HanseiBox/_user/templates', '/mnt/d/sjyoo/Study/DjangoMovie/HanseiBox/_movie/templates',],
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

WSGI_APPLICATION = 'HanseiBox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/' # CSS 디렉토리 

AUTH_USER_MODEL = 'auth.User' #유저

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/mnt/d/sjyoo/Study/DjangoMovie/HanseiBox/_user/static',
    '/mnt/d/sjyoo/Study/DjangoMovie/HanseiBox/_movie/static'
] # CSS 저장되는 경로

ROOT_URLCONF = 'HanseiBox.urls' # ?? / URL 이스케이핑하다가 나옴

LOGIN_REDIRECT_URL = '/_user/' #로그인 subApp

LOGIN_URL = '/main/login/' # 로그인 URL

LOGIN_REDIRECT_URL = '/main/profile/' # 로그인 -> 회원정보 URL

LOGOUT_REDIRECT_URL = '/main/'

MEDIA_URL = '/media/' # 이미지 저장되는 디렉토리

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # ?? / 이미지 저장되는 디렉토리 경로


