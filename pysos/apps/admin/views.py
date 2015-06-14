"""
:see: https://flask-login.readthedocs.org/en/latest/
"""
from flask import Flask, url_for, redirect, render_template, request
from flask_admin import helpers, expose
from flask_wtf import Form
from wtforms import TextField, PasswordField, validators
from werkzeug.security import generate_password_hash, check_password_hash

import flask_login as login
import flask_admin as admin

# internal
from ..attendant.models import Attendant
from ...database import db_session


class PySOSAdminView(admin.AdminIndexView):
    """

    """
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(PySOSAdminView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(PySOSAdminView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db_session.add(user)
            db_session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(PySOSAdminView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))



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

        if not user.password == self.password.data:
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

    def get_user(self):
        return db_session.query(Attendant).filter_by(
            username=self.username.data
        ).first()
