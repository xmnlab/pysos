from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import ServiceOrderStatus
from ...database import db_session


class ServiceOrderStatusView(ModelView):
    """

    """
    def __init__(self):
        super(ServiceOrderStatusView, self).__init__(
            ServiceOrderStatus, db_session
        )

    def is_accessible(self):
        return login.current_user.is_authenticated()
