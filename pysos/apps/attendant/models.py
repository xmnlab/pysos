from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)

# local
from pysos.database import Base


class Attendant(Base):
    __tablename__ = 'Atendente'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Integer, name='ateId', primary_key=True)
    name = Column(String(60), name='ateNome')
    username = Column(String(10), name='ateLogin')
    password = Column(String(10), name='ateSenha')
    enabled = Column(Integer, name='ateAtivo', server_default=text("'1'"))
    group = Column(
        String(10), name='ateGrupo', nullable=False,
        server_default=text("'publico'")
    )

    # Flask-Login integration
    def is_authenticated(self):
        return True

    # Flask-Login integration
    def is_active(self):
        return True

    # Flask-Login integration
    def is_anonymous(self):
        return False

    # Flask-Login integration
    def get_id(self):
        return self.internal_id

    def __init__(self, name=None, username=None):
        self.name = name
        self.username = username

    def __repr__(self):
        return '%s' % self.name

    # Required for administrative interface
    def __unicode__(self):
        return self.username
