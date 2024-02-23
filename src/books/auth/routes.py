from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm


auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data} "
            f"(remember me {form.remember_me.data})")
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", title="Sign In", form=form)
