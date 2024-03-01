from flask import Blueprint, render_template, request
from flask_login import login_required
from data.models import db, User
import sqlalchemy as sa

user = Blueprint("user", __name__, template_folder="templates")


@user.route("/user/<username>")
@login_required
def profile(username: str):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template("user/profile.html", user=user)
