from flask_login import UserMixin

from core import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """

    :param user_id: 

    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    """
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self) -> str:
        return self.email


class Post(db.Model):
    """ """
    __tablename__ = "posts"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"), nullable=False)
    comments = db.relationship("Comment", backref="post", lazy=True)

    def __repr__(self) -> str:
        return self.title


class Comment(db.Model):
    """ """
    __tablename__ = "comments"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)

    post_id = db.Column(db.Integer(), db.ForeignKey("posts.id"), nullable=False)

    def __repr__(self) -> str:
        return self.title
