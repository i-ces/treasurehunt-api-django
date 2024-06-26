from .base import *
print("prod")

ALLOWED_HOSTS = ["treasurehunt-api.onrender.com/"]

CSRF_TRUSTED_ORIGINS = ["https://treasurehunt-api.onrender.com/"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}
