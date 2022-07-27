from decouple import config

class Settings:
    DB_ENGINE = config('DB_ENGINE', default='sqlite')
    DB_NAME = config('DB_NAME', default='db.sqlite3')
    DB_USER = config('DB_USER', default='')
    DB_PASSWORD = config('DB_PASSWORD', default='')
    DB_HOST = config('DB_HOST', default='')
    DB_PORT = config('DB_PORT', default='')

    SECRET_KEY = config('SECRET_KEY', default='secret_key')

    DEBUG = config('DEBUG', default=False, cast=bool)
    DB_URL = '{}://{}:{}@{}:{}/{}'.format(DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    REDIS_URL = config('REDIS_URL', default='redis://localhost:6379/0')


settings = Settings()
