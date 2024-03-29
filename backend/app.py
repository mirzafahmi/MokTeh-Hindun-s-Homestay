from flask import Flask, redirect, url_for, send_from_directory
from flask_login import LoginManager, current_user, login_required
from models.models import db, AdminUser, BookedDate, HouseChoice, HouseChoices
from views.admin_views import admin_views
from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
from flask_migrate import Migrate
import os
from sqlalchemy import func
from dotenv import load_dotenv
from flask_admin.form import Select2Widget

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

class MyModelView(ModelView):
    column_list = ('house', 'client_name', 'from_book_date', 'to_book_date')
    column_default_sort = ('from_book_date', True)
    column_sortable_list = ['house', 'from_book_date', 'to_book_date', 'client_name']  # Add the columns you want to make sortable
    column_searchable_list = ['client_name']
    form_excluded_columns = ['admin_user']
    
    def on_model_change(self, form, model, is_created):
        model.admin_user = current_user
        model.admin_user_id = current_user.id

class HouseChoicesView(ModelView):
    column_list = ('name', 'status')
    form_widget_args = {
        'status': {
            'widget': Select2Widget(),
        },
    }

    def can_delete(self, model):
        return False

admin = Admin(index_view=MyAdminIndexView())

admin.add_view(HouseChoicesView(HouseChoice, db.session))
admin.add_view(MyModelView(BookedDate, db.session))

def create_app():
    app = Flask(__name__)
    CORS(app)

    load_dotenv()

    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")
    postgres_url = os.getenv("POSTGRES_URL")

    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    migrate = Migrate(app, db)
    
    @app.before_request
    def populate_house_choices():
        if not hasattr(app, 'house_choices_populated'):
            with app.app_context():
                for choice in HouseChoices:
                    house_choice = HouseChoice.query.filter_by(name=choice.name).first()
                    if not house_choice:
                        house_choice = HouseChoice(name=choice.name, status=True)
                        db.session.add(house_choice)
                db.session.commit()
                app.house_choices_populated = True

    return app

    existing_admin = AdminUser.query.filter_by(username=admin_username).first()

    if not existing_admin:
        default_admin = AdminUser(username=admin_username, password=generate_password_hash(admin_password))
        db.session.add(default_admin)
        db.session.commit()

    return app

app = create_app()
