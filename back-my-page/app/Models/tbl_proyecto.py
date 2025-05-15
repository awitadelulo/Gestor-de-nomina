from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_proyecto(Base):
    __tablename__ = "tbl_proyecto"
    id_proyecto = Column(Integer, primary_key=True, index=True)
    nombre_proyecto = Column(String(100), index=True)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    id_estado = Column(Integer, ForeignKey("tbl_estado_proyecto.id_estado"))