from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_detalle_nomina(Base):
    __tablename__ = "tbl_detalle_nomina"
    id_detalle_nomina = Column(Integer, primary_key=True, index=True)
    id_nomina = Column(Integer, ForeignKey("tbl_nomina.id_nomina"))
    concepto = Column(String(100))
    tipo = Column(String(50))
    valor = Column(DECIMAL)