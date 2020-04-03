# -*- coding: utf-8 -*-
# В Python подкаталог, содержащий файл __init__.py,
# считается пакетом и может быть импортирован. Когда вы импортируете пакет, __init__.py выполняет и определяет, какие символы предоставляют пакет для внешнего мира.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import routes, views, models