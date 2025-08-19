from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from ..extensions import db
from ..models import User
from ..utils import roles_required
from . import bp

@bp.route("/users")
@login_required
@roles_required("admin")
def users():
    rows = User.query.order_by(User.created_at.desc()).all()
    return render_template("admin/users.html", rows=rows)

@bp.route("/make-admin/<int:user_id>")
@login_required
@roles_required("admin")
def make_admin(user_id):
    u = User.query.get_or_404(user_id)
    u.role = "admin"
    db.session.commit()
    flash(f"{u.username} is now admin.", "success")
    return redirect(url_for("admin.users"))

@bp.route("/toggle-active/<int:user_id>")
@login_required
@roles_required("admin")
def toggle_active(user_id):
    u = User.query.get_or_404(user_id)
    u.is_active = not u.is_active
    db.session.commit()
    flash(f"{u.username} active={u.is_active}.", "info")
    return redirect(url_for("admin.users"))

@bp.route("/delete/<int:user_id>")
@login_required
@roles_required("admin")
def delete_user(user_id):
    u = User.query.get_or_404(user_id)
    if u.role == "admin":
        flash("Cannot delete another admin.", "warning")
        return redirect(url_for("admin.users"))
    db.session.delete(u)
    db.session.commit()
    flash("User deleted.", "success")
    return redirect(url_for("admin.users"))
