from app import db
from app.models import User, Post, Comment


def get_user(name_user):
    return User.query.filter_by(name_user=name_user).first()


def add_post(name_user, text, title):
    """
    Добавление поста
    """
    user = get_user(name_user=name_user)
    if user is None:
        user = User(name_user=name_user)
        db.session.add(user)
        id_user = get_user(name_user=name_user).get_id
    else:
        id_user = user.get_id()

    post = Post(id_user=id_user,
                text=text,
                title=title)
    db.session.add(post)
    db.session.commit()
    return True


def post_edit(id_post, text):
    """
    Редактирование поста
    """
    Post.query.filter_by(id_post=id_post).update({'text': (text)})
    db.session.commit()
    return True


def get_all_post():
    """
    Получение всех постов
    """
    posts = db.session.query(Post, User).outerjoin(User, User.id_user == Post.id_user).all()

    res = []
    d = {}
    for post in posts:
        res.append({
            'id': row[0].get('id_post'),
            'title': row[0].get('title'),
            'text': row[0].get('text'),
            'name_user': row[1].get('name_user'),
            'comments': [{

            }]
        })

    return True


