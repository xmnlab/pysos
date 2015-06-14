from flask_admin.contrib.sqla import ModelView

import flask_login as login

# internal
from .models import Attendant
from ...database import db_session


class AttendantView(ModelView):
    """

    """
    def __init__(self):
        super(AttendantView, self).__init__(Attendant, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
