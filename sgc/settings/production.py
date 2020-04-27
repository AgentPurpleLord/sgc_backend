from .base import *

DEBUG = False

WAGTAILAPI_BASE_URL = "https://startgamecrusaders.com/"

try:
    from .local import *
except ImportError:
    pass
