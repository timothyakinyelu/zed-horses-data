import os


class Config:
    """Set Flask config variables."""

    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ZED_API_KEY = os.environ.get('ZED_API_KEY')
    DEBUG=True