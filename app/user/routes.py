from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..forms import ProfileForm
from ..extensions import db
from . import bp

@bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.email = form.email.data
        db.session.commit()
        flash("Profile updated.", "success")
        return redirect(url_for("user.profile"))
    return render_template("user/profile.html", form=form, user=current_user)
