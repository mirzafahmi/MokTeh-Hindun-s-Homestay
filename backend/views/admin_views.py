from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, send_from_directory, current_app
from flask_login import login_user, logout_user, login_required
from models.models import db, AdminUser, BookedDate
from datetime import datetime
from flask_admin import Admin
import json
import os

admin = Admin()

admin_views = Blueprint('admin_views', __name__)

@admin_views.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = AdminUser.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect('admin/')
        else:
            flash('Login failed. Check your username and password.', 'error')

    return render_template('admin_login.html')

@admin_views.route('/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('admin_views.admin_login'))

@admin_views.route('/', methods=['GET'])
def data():
    with open('homestays_list.json', 'r') as f:
        data = json.load(f)

    return jsonify(data)

@admin_views.route('/media/<house_folder>/<path:filename>')
def media(house_folder, filename):
    house_path = os.path.join(current_app.config['MEDIA_FOLDER'], house_folder)
    return send_from_directory(house_path, filename)