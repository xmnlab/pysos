from flask import (
    Flask, request, url_for, redirect, render_template,
    flash, session, g, abort
)
from flask_babel import Babel, get_translations, refresh, gettext
from flask_admin import Admin, AdminIndexView
from flask_login import LoginManager
from flask_zurb_foundation import Foundation

import flask_admin as admin

# internal
from .database import db_session
# models
from .apps.attendant.models import Attendant
# views
from .apps.admin.views import LoginForm, AdminView
from .apps.attendant.views import AttendantView
from .apps.client.views import ClientView
from .apps.device_model.views import DeviceModelView
from .apps.device_brand.views import DeviceBrandView
from .apps.mobile_operator.views import MobileOperatorView
from .apps.service_order_status.views import ServiceOrderStatusView
from .apps.service_order.views import ServiceOrderView

UPLOADS_DEFAULT_DEST = '/tmp/'
MAX_CONTENT_LENGTH = 20 * 1024 * 1024

app = Flask(
    __name__,
    template_folder='public/templates',
    static_folder='public/static'
)

app.config.from_object(__name__)
app.secret_key = (
    '9\xecv\xc4\xdb\xf7\x94a\xd1Q\xd1' +
    '\x9a\x10\xfc3\xe8{\\zxp\xa1o\x90'
)

app.config['BABEL_DEFAULT_TIMEZONE'] = 'America/Sao_Paulo'
app.config['BABEL_DEFAULT_LOCALE'] = 'pt'

babel = Babel(app, default_locale='pt')

refresh()

# login
login_manager = LoginManager()
login_manager.init_app(app)

# admin
admin = admin.Admin(app, 'PySOS')  # base_template='layout.html'
admin.add_view(AttendantView())
admin.add_view(ClientView())
admin.add_view(DeviceModelView())
admin.add_view(DeviceBrandView())
admin.add_view(MobileOperatorView())
admin.add_view(ServiceOrderStatusView())
admin.add_view(ServiceOrderView())

# foundation style
Foundation(app)


# Flask views
@app.route('/')
def index():
    return '<a href="/login">Click me to get to Admin!</a>'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(userid):
    return Attendant.get(userid)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    :see: http://flask.pocoo.org/snippets/64/
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        flash(u'Successfully logged in as %s' % form.user.username)
        session['user_id'] = form.user.id
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
