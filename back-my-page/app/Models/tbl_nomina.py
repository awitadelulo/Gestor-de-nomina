from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_nomina(Base):
    __tablename__ = "tbl_nomina"
    id_nomina = Column(Integer, primary_key=True, index=True)
    id_empleado = Column(Integer, ForeignKey("tbl_empleados.id_empleado"))
    fecha_nomina = Column(Date)
    periodo = Column(String(50))