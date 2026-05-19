from base_user_settings.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Дополнительные настройки для разработки
INTERNAL_IPS = ['127.0.0.1']  # для django-debug-toolbar
