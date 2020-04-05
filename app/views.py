from flask import render_template, redirect, session, url_for, request, g
from app import app, db
from app.models import User, Post, Comment

class BaseController():

    @app.route('add_post')
    def add_post(self, **kwargs):
        user = User.query.filter_by(name_user=kwargs.get('name_user')).first()
        if user is None:
            user = User(name_user=kwargs.get('name_user'))
            session.add(user)
            id_user = User.query.filter_by(name_user=kwargs.get('name_user')).get_id()
        else:
            id_user = user.get_id()

        post = Post(id_user=id_user,
                    text=kwargs.get('text'),
                    title=kwargs.get('title'))
        db.session.add(post)
        db.commit()
        return True

