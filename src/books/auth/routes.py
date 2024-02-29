from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from extensions import db
from data.models import User
from urllib.parse import urlsplit


auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password.")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            return redirect(url_for("main.index"))
        return redirect(next_page)
    return render_template("auth/login.html", title="Sign In", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!",
              "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title="Register", form=form)
