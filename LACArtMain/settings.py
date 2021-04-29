import os
import dj_database_url
import environ
from pathlib import Path

env = environ.Env()

environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = ['127.0.0.1', 'db-artprofile.herokuapp.com']


INSTALLED_APPS = [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    
    'modelcluster',
    'taggit',
    
    'jet.dashboard',
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'blocks',
    'core',
    'crispy_forms',
    'cart',
    'staff',
]

JET_DEFAULT_THEME = 'light-violet'
JET_SIDE_MENU_COMPACT = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LACArtMain.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'LACArtMain.wsgi.application'

WAGTAIL_SITE_NAME = 'My Example Site'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap4'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_LIVE_CLIENT_ID')
PAYPAL_SECRET_KEY = os.environ.get('PAYPAL_LIVE_SECRET_KEY')
# PAYPAL_SB_CLIENT_ID= os.environ.get('PAYPAL_SB_CLIENT_ID')
# PAYPAL_SB_SECRET_KEY= os.environ.get('PAYPAL_SB_SECRET_KEY')

if DEBUG is False:
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['127.0.0.1', 'lacreates.herokuapp.com']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = True
NOTIFY_EMAIL = os.environ.get('NOTIFY_EMAIL')
EMAIL_HOST_USER = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True


AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age-9460800',
}

# Kill all AWS settings to use local CSS
# But remember to upload css on S3 bucket

# AWS_STORAGE_BUCKET_NAME = 'lacreates'
# AWS_S3_REGION_NAME = 'eu-west-2'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_S3_CUSTOM_DOMAIN = 'lacreates.s3.amazonaws.com'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = False

# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATICFILES_LOCATION = 'static/'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
# MEDIAFILES_LOCATION = 'media'

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
