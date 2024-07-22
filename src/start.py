from flask import current_app, Blueprint, render_template, request, redirect, url_for

bp = Blueprint("start", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        current_app.logger.info(f"Got things: {request.form['username']}")
        return redirect(url_for("start.loading"))

    return render_template("start/index.html")

@bp.route("/loading")
def loading():
    return "Loading"