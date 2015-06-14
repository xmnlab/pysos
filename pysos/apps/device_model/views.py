from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import DeviceModel
from ...database import db_session


class DeviceModelView(ModelView):
    """

    """
    def __init__(self):
        super(DeviceModelView, self).__init__(DeviceModel, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
