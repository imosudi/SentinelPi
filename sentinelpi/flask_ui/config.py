import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    MQTT_BROKER_URL = os.environ.get('MQTT_BROKER_URL') or 'mqtt://localhost:1883'
    MQTT_USERNAME = os.environ.get('MQTT_USERNAME')
    MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD')
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
    WIREGUARD_CONFIG_PATH = os.environ.get('WIREGUARD_CONFIG_PATH') or '/etc/wireguard/wg0.conf'
    TLS_CERT_PATH = os.environ.get('TLS_CERT_PATH') or '/etc/ssl/certs/fullchain.pem'
    TLS_KEY_PATH = os.environ.get('TLS_KEY_PATH') or '/etc/ssl/private/privkey.pem'