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
    login = Column(String(10), name='ateLogin')
    password = Column(String(10), name='ateSenha')
    enabled = Column(Integer, name='ateAtivo', server_default=text("'1'"))
    group = Column(
        String(10), name='ateGrupo', nullable=False,
        server_default=text("'publico'")
    )

    def __init__(self, name=None, login=None):
        self.name = name
        self.login = login

    def __repr__(self):
        return '%s' % self.name
