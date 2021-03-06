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
        id_user = get_user(name_user=name_user).get_id_user
    else:
        id_user = user.get_id_user

    post = Post(id_user=id_user,
                text=text,
                title=title)
    db.session.add(post)
    db.session.commit()
    return True


def post_edit(id_post, text=None):
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
    posts = db.session.query(Post, User).join(User, User.id_user == Post.id_user).all()
    comments = db.session.query(Comment).all()

    res = []

    for post in posts:
        com_for_post = list(filter(lambda x: x.get_id_post == post[0].get_id_post, comments))
        d = {
            'id': post[0].get_id_post,
            'title': post[0].get_title,
            'text': post[0].get_text,
            'name_user': post[1].get_name_user,
            'comments': [{
                'comment': p.get_comment} for p in com_for_post
            ]
        }
        res.append(d)

    return res


def add_comment_to_post(id_post, comment=None):
    """
    Добавление коментария
    """
    if not comment:
        return False

    com = Comment(comment=comment,
                  id_post=id_post)
    db.session.add(com)
    db.session.commit()
    return True


