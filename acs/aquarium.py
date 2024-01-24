from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from .auth import login_required
from .db import get_db

bp = Blueprint("aquarium", __name__, url_prefix="/aquarium")

@bp.route("/")
def index():
    """Log in a registered user by adding the user id to the session."""
    return render_template("aquarium/index.html")

@bp.route("/home")
def home():
    """Log in a registered user by adding the user id to the session."""
    return render_template("aquarium/home.html")

@bp.route("/hello2")
def hello():
    return "Hello, World2!"

@bp.route("/test")
def test():
    """Log in a registered user by adding the user id to the session."""
    return render_template("aquarium/index.html")
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                # The username was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"User {username} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("aquarium.index"))