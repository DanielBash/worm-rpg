from evennia.settings_default import *

SERVERNAME = "worm-rpg"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = ['worm.ibashlhr.beget.tech', 'localhost', '127.0.0.1']

WEBSOCKET_CLIENT_URL = "wss://worm.ibashlhr.beget.tech/ws"

try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
