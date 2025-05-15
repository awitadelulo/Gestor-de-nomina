from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# tbl_proyecto
class tbl_proyecto_schema(BaseModel):
    id_proyecto: int
    nombre_proyecto: str
    fecha_inicio: date
    fecha_fin: date
    id_estado: int

    class Config:
        orm_mode = True