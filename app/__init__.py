# -*- coding: utf-8 -*-
# В Python подкаталог, содержащий файл __init__.py,
# считается пакетом и может быть импортирован. Когда вы импортируете пакет, __init__.py выполняет и определяет, какие символы предоставляют пакет для внешнего мира.
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, views, models, errors