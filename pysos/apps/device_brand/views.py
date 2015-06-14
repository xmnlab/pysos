from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import DeviceBrand
from ...database import db_session


class DeviceBrandView(ModelView):
    """

    """
    def __init__(self):
        super(DeviceBrandView, self).__init__(DeviceBrand, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
