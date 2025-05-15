from sqlalchemy import Column, Integer, String
from app.database import Base

class tlb_estado_proyecto(Base):
    __tablename__ = "tbl_estado_proyecto"
    id_estado = Column(Integer, primary_key=True, index=True)
    descripcion= Column(String(100), index=True)