from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)

# local
from pysos.database import Base


class Product(Base):
    __tablename__ = 'Produto'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Integer, name='proId', primary_key=True)
    vendor = Column(Integer, name='proFabricante')
    product_type = Column(Integer, name='proTipoProduto', nullable=False)
    description = Column(String(60), name='proDescricao', nullable=False)
    bar_code = Column(String(60), name='proCodigoBarra')
    quantity = Column(
        Integer, name='proQtde', nullable=False, server_default=text("'0'")
    )
    quantity_min = Column(
        Integer, name='proQtdeMin', nullable=False, server_default=text("'0'")
    )
    price = Column(
        Float, name='proValor', nullable=False, server_default=text("'0'")
    )
    device_model = Column(Integer, name='proModelo')

    def __init__(self, description=None):
        self.description = description

    def __repr__(self):
        return '%s' % self.description


class ProductLocation(Base):
    __tablename__ = 'ProdutoLocalizacao'
    __table_args__ = {'schema': 'xsos'}

    product_id = Column(
        Integer, name='plcProduto', primary_key=True, nullable=False
    )
    location_id = Column(
        Integer, name='plcLocalizacao', primary_key=True, nullable=False
    )
