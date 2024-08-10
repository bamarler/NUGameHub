# settings_test.py

from .settings import *

# Test database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_test.sqlite3',  # This can be version-controlled
    }
}

DEBUG = True
