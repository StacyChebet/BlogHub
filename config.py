import os

class Config:
    '''
    Configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CHOCOLATE'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://stacy:stacy@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    DEBUG = True
    ENV = 'development'

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
