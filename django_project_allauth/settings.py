#JOSE GUADALUPE NEGRETE HERNANDEZ
import os # agregar
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-vi&o%w&&!=v&w!sab9x1n!d70c%#0i195fj-kn!gpsxc$2^cys"
DEBUG = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # agregar, Ya que es requerido por allauth
    #Apps de Allauth
    "allauth",  # agregar
    "allauth.account",  # agregar
    "allauth.socialaccount",  # agregar
]
SITE_ID = 1  # agregar, Requerido por django-allauth
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend", 
    "allauth.account.auth_backends.AuthenticationBackend",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware", # Requerido por allauth
]
ROOT_URLCONF = "django_project_allauth.urls" 
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"], #Carpeta central de plantillas, Modificar si es necesario
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
#Configuracion de Allauth (Redirecciones)
LOGIN_REDIRECT_URL = "/"  # Redirigir a la página principal después del inicio de sesión
LOGOUT_REDIRECT_URL = "/accounts/login/"  # Redirigir a la página de inicio de sesión después del cierre de sesión
ACCOUNT_LOGOUT_ON_GET = True  # Cerrar sesión con una solicitud GET
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SESSION_REMEMBER = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
WSGI_APPLICATION = "django_project_allauth.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"