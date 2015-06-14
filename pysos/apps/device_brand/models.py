from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)
from sqlalchemy.dialects.mysql.base import MEDIUMBLOB

# local
from pysos.database import Base


class DeviceBrand(Base):
    __tablename__ = 'Marca'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Integer, name='marId', primary_key=True)
    name = Column(String(15), name='marNome')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '%s' % self.name
