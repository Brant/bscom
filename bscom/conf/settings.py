from .base_settings import *

try:
    from .my_settings import *
except ImportError:
    pass

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ( "debug_toolbar", )
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
