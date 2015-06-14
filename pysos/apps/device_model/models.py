from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)
from sqlalchemy.dialects.mysql.base import MEDIUMBLOB

# local
from pysos.database import Base


class DeviceModel(Base):
    __tablename__ = 'Modelo'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Float(asdecimal=True), name='modId', primary_key=True)
    name = Column(String(20), name='modNome')
    brand = Column(ForeignKey('xsos.Marca.marId'), name='modMarca', index=True)
    image = Column(MEDIUMBLOB, name='modImagem')

    def __init__(self, name=None, brand=None):
        self.name = name
        self.brand = brand

    def __repr__(self):
        return '%s' % self.name
