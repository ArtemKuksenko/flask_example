# -*- coding: utf-8 -*-
# routes — это разные URL-адреса, которые приложение реализует
from flask import render_template, flash, redirect  # зависимость для шаблонов
from app import app

from app.forms import AddPostForm, AddCommentForm, EditPostForm
from app.views import add_post


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
        print(form.data.get('id'))
        print(form.data.get('comment'))
        return redirect('/index')

    edit = EditPostForm()

    posts = [
        {
            'id': 0,
            'name_user': 'По',
            'title': 'Жизнь дома',
            'text': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                       labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
                        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
                        velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident
                        , sunt in culpa qui officia deserunt mollit anim id est laborum.""",
            'comments': [
                {'comment': 'в само сердечко'},
                {'comment': 'до слез'},
                {'comment': 'брат за Барата'},
                {'comment': 'брат за Мурата'},
            ],
        },
        {
            'id': 1,
            'name_user': 'По2',
            'title': 'Жизнь дома2',
            'text': """2Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                           labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
                            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
                            velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident
                            , sunt in culpa qui officia deserunt mollit anim id est laborum.""",
            'comments': [
                {'comment': 'в само сердечко2'},
                {'comment': 'до слез2'},
                {'comment': 'брат за Барата2'},
                {'comment': 'брат за Мурата2'},
            ],
        },
    ]
    for p in posts:
        p['form'] = AddCommentForm()
        p['form'].id.default = p['id']
        p['form'].process()
        p['edit'] = EditPostForm()
        p['edit'].id.default = p['id']
        p['edit'].process()

    return render_template('index.html', title='Home', posts=posts)


