from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)

# local
from pysos.database import Base


class Client(Base):
    __tablename__ = 'Cliente'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(Float(asdecimal=True), name='cliId', primary_key=True)
    name = Column(String(60), name='cliNome')
    enterprise_register_number = Column(String(19), name='cliCnpj')
    personal_register_number = Column(String(11), name='cliCpf')
    personal_optional_register_number = Column(String(9), name='cliRg')
    personal_optional_register_issuing_institution = (
        Column(String(10), name='cliOrgaoemissorrg')
    )
    address = Column(String(60), name='cliEndereco')
    district = Column(String(25), name='cliBairro')
    city = Column(String(30), name='cliCidade')
    state = Column(String(2), name='cliUf')
    zip_code = Column(String(8), name='cliCep')
    phone1 = Column(String(15), name='cliFone1')
    phone2 = Column(String(15), name='cliFone2')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '%s' % self.name
