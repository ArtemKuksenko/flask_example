# -*- coding: utf-8 -*-
# routes — это разные URL-адреса, которые приложение реализует
from flask import render_template # зависимость для шаблонов
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Сидим дома на самоизоляции!"

@app.route('/template')
def template():
    user = {'username': 'Даша путешственница'}
    homebodies = ['По', 'Ляля', 'Тинки-Винки', 'Дипси']
    return render_template('template.html', title='Home', user=user, homebodies=homebodies)
