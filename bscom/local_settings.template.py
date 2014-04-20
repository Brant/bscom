# Rename me to local_settings.py

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    MY_EMAIL = ''
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = ''
    SERVER_EMAIL = ''

    ALLOWED_HOSTS = ['.brantsteen.com', ]

DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


