from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# Tomado de la ayuda de Heroku
# https://devcenter.heroku.com/articles/django-assets
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-@g*m6n6zcewman&$8t-iqxfy*l10&k#f#c9huf6%)-%-f=o-xv'  # Esta línea se creó por defecto. Generé una nueva SECRET_KEY, y la guardé en .env
SECRET_KEY = str(os.getenv('SECRET_KEY'))


# https://phys-eval.herokuapp.com/
# Mirror in
# https://github.com/gianfranco-s/physEvHeroku.git
DEBUG = False

ALLOWED_HOSTS = ['*']

# CORS
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ALLOWED_ORIGINS = [
        "https://boiling-cove-03768.herokuapp.com/",
        "http://127.0.0.1:8000",
        "http://0.0.0.0:5000",
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ejercicios',
    'usuarios',
    'rest_framework',
    # 'corsheaders',
]

MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'physicsEval.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'physicsEval.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {

            # -----------------------------------------------------------------------------------
            # Para hacer debug localmente, estoy teniendo que descomentar estas dos líneas
            'ENGINE': 'django.db.backends.sqlite3',    # Venía por defecto al crear el proyecto.
            'NAME': BASE_DIR + 'db.sqlite3',           # Venía por defecto al crear el proyecto.
            # -----------------------------------------------------------------------------------
        }
    }
else:
    DATABASES = {
        'default': {
            # -----------------------------------------------------------------------------------
            # Para que ande en Heroku, usar PostgreSQL
            
            # Estos datos se encuentran dentro ed UNA variable en settings en Heroku (reveal config vars)
            'ENGINE': 'django.db.backends.postgresql',
            'NAME' : 'd5q0plajcpuhe5',
            'HOST' : 'ec2-44-196-8-220.compute-1.amazonaws.com:',
            'PORT' : 5432,
            'USER' : 'lajyylaixxblil',
            'PASSWORD': '0f7ca38b6ff65dbcd643d8c802ab4fca472a9e6cfea4d3aac8107f8910762df6',
            # -----------------------------------------------------------------------------------
        }
    }




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Tomado de la ayuda de Heroku
# https://devcenter.heroku.com/articles/django-assets
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

# Según django-Girls, para archivos estáticos (no me anduvo):
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Según ordinary-coders (anduvo, pero en Heroku lo hacen diferente):
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), ]

# Tomado de la ayuda de Heroku
# https://devcenter.heroku.com/articles/django-assets
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure Django App for Heroku.
import django_on_heroku
django_on_heroku.settings(locals())


