from app import db
from app.models import User, Post, Comment


def get_user(name_user):
    return User.query.filter_by(name_user=name_user).first()


def get_all_user():
    return User.query.all()


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
    res = get_all_post()
    db.session.commit()
    return True


def get_all_post():
    """
    Получение всех постов
    """
    posts = db.session.query(Post, User).join(User, User.id_user == Post.id_user).all()
    comments = db.session.query(Comment).all()

    res = []

    for post in posts:
        com_for_post = list(filter(lambda x: x['id_post'] == post[0].get_id, comments))
        d = {
            'id': post[0].get('id_post'),
            'title': post[0].get('title'),
            'text': post[0].get('text'),
            'name_user': post['author'].get('name_user'),
            'comments': [{
                'comment': p.get('comment')} for p in com_for_post
            ]
        }
        res.append(d)

    return True


