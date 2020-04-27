from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = '^ld6x(%wz3%0--$5&cc9jydadh7f#v6e*8%a@foq&*2z#@y&zc'

WAGTAILAPI_BASE_URL = "https://startgamecrusaders.com/"
BASE_URL = 'https://startgamecrusaders.com'
USE_X_FORWARDED_HOST = True

try:
    from .local import *
except ImportError:
    pass
