# файл конфигурации
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'home-home'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
