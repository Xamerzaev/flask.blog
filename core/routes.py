from flask import render_template, request, redirect, url_for
from flask_login import logout_user, login_required, current_user, login_user

from core import app
from core.models import db, User, Post, Comment
from core.forms import RegForm, PostForm


@app.route("/")
def index():
    """ """
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    """ """
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for("index"))
        else:
            print("Ошибка")
    return render_template("login.html")


@app.route("/reg", methods=["GET", "POST"])
def reg():
    """ """
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegForm()
    if request.method == "POST":
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("reg.html", form=form)


@app.route("/logout")
@login_required
def logout():
    """ """
    logout_user()
    return redirect("index.html")


@app.route("/add_post", methods=["GET", "POST"])
@login_required
def new_post():
    """ """
    form = PostForm()
    if request.method == "POST":
        post = Post(
            title=form.title.data, content=form.content.data, user_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html", form=form)


@app.route("/blog_single/<int:post_id>", methods=["GET", "POST"])
def blog_single(post_id):
    """

    :param post_id: 

    """
    post = Post.query.get(post_id)
    comments = post.comments
    if request.method == "POST":
        comment = Comment(title=request.form.get("title"), post=post)
        db.session.add(comment)
        db.session.commit()
    return render_template("blog_single.html", post=post, comments=comments)
