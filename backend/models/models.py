from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timedelta, timezone

db = SQLAlchemy()

current_date = datetime.now

class AdminUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    create_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone(timedelta(hours=8))))
    update_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone(timedelta(hours=8))), onupdate=lambda: datetime.now(timezone(timedelta(hours=8))))

class BookedDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(20), nullable=False)
    from_book_date = db.Column(db.DateTime, nullable=False)
    to_book_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone(timedelta(hours=8))))
    update_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone(timedelta(hours=8))), onupdate=lambda: datetime.now(timezone(timedelta(hours=8))))
    admin_user_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'))
    admin_user = db.relationship('AdminUser', backref='booked_dates')
