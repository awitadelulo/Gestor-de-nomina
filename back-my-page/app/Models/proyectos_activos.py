# app/models/vw_proyectos_activos.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class vw_proyectos_activos(Base):
    __tablename__ = "vw_proyectos_activos"
    __table_args__ = {'extend_existing': True}

    id_proyecto = Column(Integer, primary_key=True)
    nombre_proyecto = Column(String)
    estado = Column(String)