# файл конфигурации
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'home-home'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')  # путь к файлу с нашей базой данных
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # папка, где мы будем хранить файлы SQLAlchemy-migrate
    SQLALCHEMY_TRACK_MODIFICATIONS = False

