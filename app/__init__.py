import os
from datetime import datetime, timezone
from hmac import compare_digest
from secrets import token_urlsafe
from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    body = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    author = db.relationship("User", backref="posts")

@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session.get(User, int(user_id))
    except (TypeError, ValueError):
        return None

def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY") or token_urlsafe(32),
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///social.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAX_CONTENT_LENGTH=16384,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )
    if config:
        app.config.update(config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    @app.context_processor
    def inject_csrf():
        if "_csrf" not in session:
            session["_csrf"] = token_urlsafe(32)
        return {"csrf_token": session["_csrf"]}

    @app.before_request
    def csrf_protection():
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            if not compare_digest(session.get("_csrf", ""), request.form.get("_csrf", "")) or not session.get("_csrf"):
                abort(400)

    @app.get("/")
    def feed():
        posts = db.session.execute(select(Post).order_by(Post.created_at.desc(), Post.id.desc()).limit(100)).scalars().all()
        return render_template("feed.html", posts=posts)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("feed"))
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            if not (3 <= len(username) <= 30 and username.isascii() and username.replace("_", "").isalnum()):
                flash("Use 3–30 ASCII letters, digits or underscores.", "error")
            elif len(password) < 8:
                flash("Password must have at least 8 characters.", "error")
            elif db.session.execute(select(User).filter_by(username=username)).scalar_one_or_none():
                flash("Username already taken.", "error")
            else:
                user = User(username=username, password_hash=generate_password_hash(password))
                db.session.add(user)
                try:
                    db.session.commit()
                except Exception:
                    db.session.rollback()
                    flash("Registration failed. Try a different username.", "error")
                else:
                    login_user(user)
                    return redirect(url_for("feed"))
        return render_template("auth.html", mode="register")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("feed"))
        if request.method == "POST":
            user = db.session.execute(select(User).filter_by(username=request.form.get("username", "").strip())).scalar_one_or_none()
            if user and check_password_hash(user.password_hash, request.form.get("password", "")):
                login_user(user)
                return redirect(url_for("feed"))
            flash("Invalid username or password.", "error")
        return render_template("auth.html", mode="login")

    @app.post("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("feed"))

    @app.post("/posts")
    @login_required
    def create_post():
        body = request.form.get("body", "").strip()
        if not 1 <= len(body) <= 280:
            flash("Posts must be 1–280 characters.", "error")
        else:
            db.session.add(Post(author_id=current_user.id, body=body))
            db.session.commit()
            flash("Post published.", "success")
        return redirect(url_for("feed"))

    with app.app_context():
        db.create_all()
    return app
