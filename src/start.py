from flask import current_app, Blueprint, render_template, request, redirect, url_for, session

bp = Blueprint("start", __name__)

@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        session.clear()
        session["userId"] = request.form["username"]
        
        current_app.logger.info(f"Got username: {session.get('userId')}")
        return redirect(url_for("start.loading"))

    return render_template("start/index.html")

@bp.route("/loading")
def loading():
    current_app.logger.info(f"Session: {session.get('userId')}")
    return render_template("start/loading.html")