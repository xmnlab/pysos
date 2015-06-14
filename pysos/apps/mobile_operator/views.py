from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import MobileOperator
from ...database import db_session


class MobileOperatorView(ModelView):
    """

    """
    def __init__(self):
        super(MobileOperatorView, self).__init__(MobileOperator, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
