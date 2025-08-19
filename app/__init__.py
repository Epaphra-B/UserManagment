from flask import Flask, render_template
from .extensions import db, login_manager, migrate, csrf
from .models import User

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))

    # Blueprints
    from .auth.routes import bp as auth_bp
    from .user.routes import bp as user_bp
    from .admin.routes import bp as admin_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    # Simple index
    @app.get("/")
    def index():
        return render_template("index.html", title="Home")

    return app
