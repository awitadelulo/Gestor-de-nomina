from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_detalle_liquidacion(Base):
    __tablename__ = "tbl_detalle_liquidacion"
    id_detalle_liquidacion = Column(Integer, primary_key=True, index=True)
    id_liquidacion = Column(Integer, ForeignKey("tbl_liquidacion.id_liquidacion"))
    concepto = Column(String(100))
    tipo = Column(String(50))
    valor = Column(DECIMAL)