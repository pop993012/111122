"""
Django settings for untitled7 project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR,'apps'))
sys.path.append(os.path.join(BASE_DIR,'extr_apps'))
sys.path.append(os.path.join(BASE_DIR,'untitled7'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kh1m4*a9t16c9(^ns=9y^dud%*zj145b4tpx2(x8$)7=-bbqzh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'xadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'apps.goods',
    'apps.trade',
    'apps.user',
    'apps.social_django',
     'front',
    'apps.user_operation',
    'rest_framework',
    'django_filters',
   'DjangoUeditor',
    'coreschema',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
   # 'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'untitled7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')] ,

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
'social_django.context_processors.backends',
  'social_django.context_processors.login_redirect',
                 #'rest_framework_jwt',

            ],
        },
    },
]
APPEND_SLASH=False
WSGI_APPLICATION = 'untitled7.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # mysql数据库
        'NAME': 'test', # 数据库的名字
        'USER': 'root', # 数据库的用户名
        'PASSWORD': 'root', # 数据库的密码
        'HOST': '127.0.0.1', # ip地址
        'PORT': '3306', # 数据库的端口号
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

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

AUTH_USER_MODEL = 'user.User'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
#STATIC_ROOT=os.path.join(BASE_DIR,"static")

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

# REST_FRAMEWORK = {
#
#   'DEFAULT_AUTHENTICATION_CLASSES': (
#
#       'rest_framework.authentication.BasicAuthentication',
#
#       'rest_framework.authentication.SessionAuthentication',
#
#       'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#
#   )
#
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 添加jwt验证类
#
#     ),
# }
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://106.13.123.167:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "123456aa",
        },
    },
}


# AUTHENTICATION_BACKENDS = [  'apps.user.views.CustomBackend',]
AUTHENTICATION_BACKENDS = [
    'user.views.CustomBackend',
    'social_core.backends.weibo.WeiboOAuth2',
    #'social_core.backends.qq.QQOAuth2',
    #'social_core.backends.weixin.WeixinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',                       #JWT跟前端保持一致，比如“token”这里设置成JWT
}

# WEIBO_APP_ID=''
# WEIBO_KEY = '5e81fca1ca5b7d19f516454667ccdf7a'
# WEIBO_CALLBACK_URL = 'http://47.105.128.181:8000.0.0.1:8000/oauth/weibo_check'
SOCIAL_AUTH_WEIBO_KEY = '2878595388'
SOCIAL_AUTH_WEIBO_SECRET = '5e81fca1ca5b7d19f516454667ccdf7a'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://47.105.128.181/aa/'



