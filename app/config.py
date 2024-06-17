class Config:
    DEBUG = True
    SECRET_KEY = 'secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pi-block-explorer.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATE_LIMITER_ENABLED = True
    RATE_LIMITER_MAX_REQUESTS = 100
    RATE_LIMITER_TIME_WINDOW = 60
    WEBHOOK_ENABLED = True
    WEBHOOK_URL = 'https://example.com/webhook'
