# -*- coding: utf-8 -*-
# routes — это разные URL-адреса, которые приложение реализует
from flask import render_template, flash, redirect  # зависимость для шаблонов
from app import app

from app.forms import AddPostForm, AddCommentForm, EditPostButton, EditPostForm
from app.views import add_post, post_edit, get_all_post, add_comment_to_post


@app.route('/hello_home')
# приметивный базовый пример
def hello_home():
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

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_post(id):
    form = EditPostForm()
    if form.validate_on_submit():
        post_edit(id_post=id,
                  text=form.data.get('text'))
        return redirect('/index')
    return render_template('edit_post.html', title='ред.пост', form=form)

@app.route('/create', methods=['GET', 'POST'])
def add_post_route():
    form = AddPostForm()
    if form.validate_on_submit():
        add_post(name_user=form.data.get('name_user'),
                 title=form.data.get('title'),
                 text=form.data.get('text'))
        print(form.data.get('name_user'))
        return redirect('/index')
    return render_template('add_post.html', title='+пост', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = AddCommentForm()

    if form.validate_on_submit():
        add_comment_to_post(id_post=form.data.get('id'),
                            comment=form.data.get('comment'))
        return redirect('/index')

    edit = EditPostButton()
    if edit.validate_on_submit():
        return redirect(f"/edit/{edit.data.get('id')}")

    posts = get_all_post()

    for p in posts:
        p['form'] = AddCommentForm()
        p['form'].id.default = p['id']
        p['form'].process()
        p['edit'] = EditPostButton()
        p['edit'].id.default = p['id']
        p['edit'].process()

    return render_template('index.html', title='Home', posts=posts)


