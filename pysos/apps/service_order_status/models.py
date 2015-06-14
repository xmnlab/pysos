from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)

# local
from pysos.database import Base


class ServiceOrderStatus(Base):
    __tablename__ = 'EstadoOs'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Integer, name='etoId', primary_key=True)
    name = Column(String(60), name='etoNome', nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '%s' % self.name
