from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# tbl_tipo_contrato
class tbl_tipo_contrato_schema(BaseModel):
    id_tipo_contrato: int
    descripcion: str

    class Config:
        orm_mode = True