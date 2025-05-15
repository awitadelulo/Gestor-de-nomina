from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class tbl_detalle_nomina_schema(BaseModel):
    id_detalle_nomina: int
    id_nomina: int
    concepto: str
    tipo: str
    valor: Decimal

    class Config:
        orm_mode = True