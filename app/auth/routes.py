from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import bp
from ..forms import RegisterForm, LoginForm
from ..models import User
from ..extensions import db

@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile"))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter((User.username==form.username.data) | (User.email==form.email.data)).first():
            flash("Username or email already exists.", "danger")
            return render_template("auth/register.html", form=form)
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please sign in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(form.password.data) or not user.is_active:
            flash("Invalid credentials.", "danger")
            return render_template("auth/login.html", form=form)
        login_user(user)
        nxt = request.args.get("next") or url_for("user.profile")
        return redirect(nxt)
    return render_template("auth/login.html", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Signed out.", "info")
    return redirect(url_for("auth.login"))
