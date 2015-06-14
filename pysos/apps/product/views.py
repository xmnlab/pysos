from flask_admin.contrib.sqla import ModelView
import flask_login as login

# internal
from .models import Product
from ...database import db_session


class ProductView(ModelView):
    """

    """
    def __init__(self):
        super(ProductView, self).__init__(Product, db_session)

    def is_accessible(self):
        return login.current_user.is_authenticated()
