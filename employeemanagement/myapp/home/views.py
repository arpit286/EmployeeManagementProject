# external
from flask import render_template, abort
from flask_login import login_required, current_user

# internal
from . import home

@home.route('/')
@home.route('/index')
def homepage():
    '''Render the home page template on the / and /index route'''
    return render_template('home/index.html', title='Welcome!')


@home.route('/dashboard')
@login_required
def dashboard():
    '''Render the dashboard template on the /dashboard route'''
    return render_template('home/dashboard.html', title='Dashboard')


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_dashboard.html', title='Dashboard')
