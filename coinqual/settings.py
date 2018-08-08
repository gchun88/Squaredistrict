"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

TIME_ZONE='UTC'
USE_TZ=True
# Other Django configurations...
# Celery application definition
# http://docs.celeryproject.org/en/v4.0.2/userguide/configuration.html
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
# Celery Codes
# The following lines may contains pseudo-code
from celery.schedules import crontab
# Other Celery settings
#CELERYBEAT_SCHEDULE = {
#    'task-number-one': {
#        'task': 'run_scheduled_jobs',
#        'schedule': crontab(),
##        'args': (*args)
#    },}
#,
#    'task-number-two': {
#        'task': 'app2.tasks.task_number_two',
#        'schedule': crontab(minute=0, hour='*/3,10-19'),
#        'args': (*args)
#    }
#}






# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='32113814922-csqtcr1qor1r5pmtj75hpf99e8mrpk8e.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='ek8OGZuEPObk2dKzTfHz4RBN'
#Quick-start development settings - unsuitable for production
#See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

#coinbase
SOCIAL_AUTH_COINBASE_KEY = '29046aae8c5602e32b88b014dccff34b68db219e8892d94f4eb3b96ecdc005cf'
SOCIAL_AUTH_COINBASE_SECRET = '20b8a63a0bdcf5c8c541a8a1bc2cdf878fa7de8c0af26eea99846db6eda28b6c'
SOCIAL_AUTH_COINBASE_SCOPE = ['wallet:accounts:read:BTC']
SOCIAL_AUTH_COINBASE_AUTH_EXTRA_ARGUMENTS = {'account': 'all'}




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z=m6c&2(t3sh*)z72n9f+o_k3(97c1avl7tlrp3!1g1^!5rucs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL= '/'

STATIC_URL = 'polls/static/'



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
#                'social_django.context_processors.backends',  # <- Here
#                'social_django.context_processors.login_redirect', # <- Here
#                'django_settings_export.settings_export',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
  # ...
  'django.core.context_processors.request',
  # ...
)






INSTALLED_APPS = [
    'django_celery_beat',
    'django_celery_results',
#    'django_extensions',
#    'sslserver',
#    'djangosecure',
    'cquser.apps.CquserConfig',
    'planner.apps.PlannerConfig',
#    'bootstrap3.bootstrap',
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'social_django',

]

AUTHENTICATION_BACKENDS=(
    'django.contrib.auth.backends.ModelBackend',
)


MIDDLEWARE = [
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES=(
    'djangosecure.middleware.SecurityMiddleware',
)

SECURE_SSL_REDIRECT = False


ROOT_URLCONF = 'coinqual.urls'


WSGI_APPLICATION = 'coinqual.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'coinqualDB',
#         'USER':'coinqual',
#         'PASSWORD': 'ChipFanBus0',
#         'HOST': 'coinqualdb.cysmygzyhtfg.us-west-1.rds.amazonaws.com',
#         'PORT': '3306'
#     }
# }
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



USE_I18N = True

USE_L10N = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'





