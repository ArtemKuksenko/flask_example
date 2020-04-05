from app import db
from app.models import User, Post, Comment


def add_post(name_user, text, title):
    user = User.query.filter_by(name_user=name_user).first()
    if user is None:
        user = User(name_user=name_user)
        db.session.add(user)
        id_user = User.query.filter_by(name_user=name_user).first().get_id
    else:
        id_user = user.get_id()

    post = Post(id_user=id_user,
                text=text,
                title=title)
    db.session.add(post)
    db.session.commit()
    return True

