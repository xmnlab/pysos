"""
:see: https://flask-login.readthedocs.org/en/latest/
"""
from flask_admin.contrib.sqla import ModelView
from flask_wtf import Form
from wtforms import TextField, PasswordField, validators

import flask_login as login
import flask_admin as admin

# internal
from ..attendant.models import Attendant
from ...database import db_session


class AdminView(admin.BaseView):
    """

    """
    @admin.expose('/')
    def index(self):
        return self.render('/admin/index.html')

    def is_accessible(self):
        """
        """
        return login.current_user.is_authenticated()


class LoginForm(Form):
    """
    :see: http://flask.pocoo.org/snippets/64/

    """
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        """

        :return:
        """
        rv = Form.validate(self)
        if not rv:
            return False

        user = Attendant.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
