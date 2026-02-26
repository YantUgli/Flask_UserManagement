import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", 'superkey')

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///users.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False