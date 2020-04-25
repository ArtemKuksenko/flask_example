from app import db

class User(db.Model):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer(), primary_key=True)
    name_user = db.Column(db.String(32), index=True, unique=True)
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, name_user):
        self.name_user = name_user

    def __repr__(self):
        return '<User {}'.format(self.name_user)

    @property
    def get_id_user(self):
        return self.id_user

    @property
    def get_name_user(self):
        return self.name_user

    @property
    def get_post(self):
        return self.post


class Post(db.Model):
    __tablename__ = 'post'
    id_post = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey('user.id_user'))
    text = db.Column(db.String(140))
    title = db.Column(db.String(32))
    comment = db.relationship('Comment', backref='user_comment', lazy='dynamic')

    def __init__(self, id_user, text, title):
        self.id_user = id_user
        self.text = text
        self.title = title

    def __repr__(self):
        return 'Post {}'.format(self.text)

    @property
    def get_id_post(self):
        return self.id_post

    @property
    def get_id_user(self):
        return self.id_user

    @property
    def get_text(self):
        return self.text

    @property
    def get_title(self):
        return self.title

    @property
    def get_comment(self):
        return self.comment


class Comment(db.Model):
    __tablename__ = 'comment'
    id_comment = db.Column(db.Integer(), primary_key=True)
    comment = db.Column(db.String(64))
    id_post = db.Column(db.Integer(), db.ForeignKey('post.id_post'))

    def __init__(self, id_post, comment):
        self.id_post = id_post
        self.comment = comment

    def __repr__(self):
        return 'Comment {}'.format(self.comment)

    @property
    def get_id_comment(self):
        return self.id_comment

    @property
    def get_id_post(self):
        return self.id_post

    @property
    def get_comment(self):
        return self.comment