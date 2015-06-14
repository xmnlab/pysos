from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text, text
)
from sqlalchemy.orm import relationship

# local
from pysos.database import Base


class ServiceOrder(Base):
    __tablename__ = 'Os'
    __table_args__ = {'schema': 'xsos'}

    internal_id = Column(
        Float(asdecimal=True), name='osxId', primary_key=True
    )
    client = Column(
        ForeignKey('xsos.Cliente.cliId'), name='osxCliente', index=True
    )
    device_hexadecimal_number = Column(
        String(15), name='osxNumeroHexadecimalAparelho'
    )
    device_line_number = Column(String(15), name='osxNumeroLinhaAparelho')
    device_line_plan = Column(String(3), name='osxPlanoAparelho')
    mobile_operator = Column(
        ForeignKey('xsos.Operadora.opeId'), name='osxOperadoraAparelho',
        index=True
    )
    device_model = Column(
        ForeignKey('xsos.Modelo.modId'), name='osxModeloAparelho', index=True
    )
    date_check_in = Column(DateTime, name='osxDtAbertura')
    date_check_out_estimated = Column(DateTime, name='osxDtEntregaPrevista')
    date_check_out = Column(DateTime, name='osxDtEntrega')
    status = Column(String(3), name='osxEstado')
    attendant = Column(
        ForeignKey('xsos.Atendente.ateId'), name='osxAtendente', index=True
    )
    client_observation = Column(Text, name='osxObsCliente')
    technical_observation = Column(Text, name='osxObsTecnica')
    service_description = Column(Text, name='osxDescricaoServico')
    service_cost = Column(
        Float(7), name='osxValorServico', server_default=text("'0.00'")
    )
    device_state = Column(Text, name='osxEstadoAparelho')
    material_cost = Column(
        Float(7), name='osxCustoMaterial', server_default=text("'0.00'")
    )

    Attendant = relationship('Attendant')
    Client = relationship('Client')
    DeviceModel = relationship('DeviceModel')
    MobileOperator = relationship('MobileOperator')

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '%s' % self.internal_id
