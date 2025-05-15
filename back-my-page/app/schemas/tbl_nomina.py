from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# tbl_nomina
class tbl_nomina_schema(BaseModel):
    id_nomina: int
    id_empleado: int
    fecha_nomina: date
    periodo: str

    class Config:
        orm_mode = True