from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_liquidacion(Base):
    __tablename__ = "tbl_liquidacion"
    id_liquidacion = Column(Integer, primary_key=True, index=True)
    id_empleado = Column(Integer, ForeignKey("tbl_empleados.id_empleado"))
    fecha_liquidacion = Column(Date)
    fecha_inicio_periodo = Column(Date)
    fecha_fin_periodo = Column(Date)
    motivo_liquidacion = Column(String(255))