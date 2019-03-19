"""
Django settings for samples project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g$iqqu&*mw4_sg3(#ld0sqaalxebel&168^yj%i&sgrw(fmn@w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'hello.apps.HelloConfig',
    'getpost.apps.GetpostConfig',
    'users.apps.UsersConfig',
    'tracks.apps.TracksConfig',
    'views.apps.ViewsConfig',
    'templates.apps.TemplatesConfig',
    'generic.apps.GenericConfig',
    'session.apps.SessionConfig',
    'form.apps.FormConfig',
    'many.apps.ManyConfig',
    'owner.apps.OwnerConfig',
    'menu.apps.MenuConfig',
]

# When we get to crispy forms :)
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samples.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'samples.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Install optional bits that depend on several pip installs
try:
    from rest_framework import serializers
    INSTALLED_APPS += [
        'rest_framework',
        'rest.apps.RestConfig',
    ]
except:
    print('Could not find rest_framework, please see requirements.txt')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

try: 
    from crispy_forms.helper import FormHelper
    INSTALLED_APPS += [
        'crispy_forms',
        'crispy.apps.CrispyConfig',
    ]
except:
    print('Could not find crispy forms, please see requirements.txt')

# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
social_installed = False
try: 
    from social_core.utils import setting_name
    social_installed = True
except:
    print('Could not find social django, please see requirements.txt')

if social_installed :
    try:
        from . import github_settings 
        SOCIAL_AUTH_GITHUB_KEY = github_settings.SOCIAL_AUTH_GITHUB_KEY
        SOCIAL_AUTH_GITHUB_SECRET = github_settings.SOCIAL_AUTH_GITHUB_SECRET

        INSTALLED_APPS += [
            'social_django',
        ]
        MIDDLEWARE += [
            'social_django.middleware.SocialAuthExceptionMiddleware',
        ]
        TEMPLATES[0]['OPTIONS']['context_processors'] += [
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
        ]
    except:
        print('Could not import github_settings.py for social_django')

# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#authentication-backends
# https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'