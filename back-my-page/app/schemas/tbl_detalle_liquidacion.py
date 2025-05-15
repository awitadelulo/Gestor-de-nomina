from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class tbl_detalle_liquidacion_schema(BaseModel):
    id_detalle_liquidacion: int
    id_liquidacion: int
    concepto: str
    tipo: str
    valor: Decimal

    class Config:
        orm_mode = True