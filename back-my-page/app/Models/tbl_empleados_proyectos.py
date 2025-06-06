from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_empleados_proyectos(Base):
    __tablename__ = "tbl_empleados_proyectos"
    id_empleado = Column(Integer, primary_key=True,autoincrement=True)
    id_proyecto = Column(Integer,autoincrement=True)
    id_tipo_contrato = Column(Integer, ForeignKey("tbl_tipo_contrato.id_tipo_contrato"), nullable=True)
    inicio_contrato = Column(Date)
    fin_contrato = Column(Date)