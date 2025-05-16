from sqlalchemy import Column, Integer, String, Float
from app.database import Base  # tu clase Base global para los modelos

class vw_detalle_nomina(Base):
    __tablename__ = "VW_DETALLE_NOMINA"  # Oracle lo guarda en mayúsculas

    id_nomina = Column(Integer, primary_key=True)
    id_empleado = Column(Integer)
    empleado = Column(String)
    concepto = Column(String)
    valor = Column(Float)