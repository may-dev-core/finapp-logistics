from config.settings.base import *

try:
    from .production import *
except expression as identifier:
    pass
else:
    from .local import *