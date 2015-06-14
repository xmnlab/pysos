from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)

# local
from pysos.database import Base


class MobileOperator(Base):
    __tablename__ = 'Operadora'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Integer, name='opeId', primary_key=True)
    name = Column(String(15), name='opeNome')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '%s' % self.name
