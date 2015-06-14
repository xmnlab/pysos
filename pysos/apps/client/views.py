from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import Client
from ...database import db_session


class ClientView(ModelView):
    """

    """
    def __init__(self):
        super(ClientView, self).__init__(Client, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
