from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import ServiceOrder
from ...database import db_session


class ServiceOrderView(ModelView):
    """

    """
    def __init__(self):
        super(ServiceOrderView, self).__init__(ServiceOrder, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
