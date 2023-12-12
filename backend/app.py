from flask import Flask, redirect, url_for, send_from_directory
from flask_login import LoginManager, current_user, login_required
from models.models import db, AdminUser, BookedDate
from views.admin_views import admin_views
from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
import os

admin = Admin()

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('admin_views.admin_login'))
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin_views.admin_login'))

admin = Admin(index_view=MyAdminIndexView())

admin.add_view(ModelView(AdminUser, db.session))
admin.add_view(ModelView(BookedDate, db.session))

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY'] = b'5473D5711462A31425AC9685C3EA6'
    MEDIA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
    app.config['MEDIA_FOLDER'] = MEDIA_FOLDER

    login_manager = LoginManager(app)
    login_manager.login_view = 'admin_login'

    @login_manager.user_loader
    def load_user(user_id):
        from models.models import db, AdminUser, BookedDate
        return AdminUser.query.get(int(user_id))

    app.register_blueprint(admin_views)

    db.init_app(app)
    admin.init_app(app)
    
    with app.app_context():
        db.create_all()

        existing_admin = AdminUser.query.filter_by(username='admin').first()

        if not existing_admin:
            default_admin = AdminUser(username='admin', password='Qwerty_12345')
            db.session.add(default_admin)
            db.session.commit()

    return app