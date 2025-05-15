from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.database import Base

class tbl_tipo_contrato(Base):
    __tablename__ = "tbl_tipo_contrato"
    id_tipo_contrato = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), index=True)