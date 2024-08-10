# settings_dev.py

from .settings import *

# Development database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_dev.sqlite3',  # Separate development database
    }
}

DEBUG = True
