# -*- coding: utf-8 -*-
# routes — это разные URL-адреса, которые приложение реализует
from flask import render_template, flash, redirect # зависимость для шаблонов
from app import app

from app.forms import LoginForm

@app.route('/hello_home')
# приметивный базовый пример
def index():
    return "HELLO HOME!"

@app.route('/template')
# шаблон, ссылка с примером ниже
# http://127.0.0.1:5000/template
def template():
    user = {'username': 'Лягушка путешественница'}
    homebodies = ['По', 'Ляля', 'Тинки-Винки', 'Дипси']
    return render_template('template.html', title='Home', user=user, homebodies=homebodies)


@app.route('/template/<username>')
# шблон, ссылка с примером ниже
# http://127.0.0.1:5000/template/%D0%9B%D1%8F%D0%B3%D1%83%D1%88%D0%BA%D0%B0%20%D0%BF%D1%83%D1%82%D0%B5%D1%88%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B8%D1%86%D0%B0
def template_id(username):
    user = {'username': username}
    homebodies = ['По', 'Ляля', 'Тинки-Винки', 'Дипси']
    return render_template('template.html', title='Home', user=user, homebodies=homebodies)

@app.route('/create', methods=['GET', 'POST'])
def add_post():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username)
        return redirect('/index')
    return render_template('add_post.html', title='+пост', form=form)