from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# tbl_liquidacion
class tbl_liquidacion_schema(BaseModel):
    id_liquidacion: int
    id_empleado: int
    fecha_liquidacion: date
    fecha_inicio_periodo: date
    fecha_fin_periodo: date
    motivo_liquidacion: str

    class Config:
        orm_mode = True