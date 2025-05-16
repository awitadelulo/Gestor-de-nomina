from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_empleados(Base):
    __tablename__ = "tbl_empleados"
    id_empleado = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(100))
    apellidos = Column(String(100))
    salario_basico = Column(DECIMAL)
    id_tipo_contrato = Column(Integer, ForeignKey("tbl_tipo_contrato.id_tipo_contrato"))
    fecha_contratacion = Column(Date) 