from flask import Blueprint
from flask import Blueprint
from flask import render_template

bp = Blueprint("base", __name__)

@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    return render_template("content.html")