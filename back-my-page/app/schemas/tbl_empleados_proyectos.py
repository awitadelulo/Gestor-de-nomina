from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# tbl_empleados_proyectos
class tbl_empleados_proyectos_schema(BaseModel):
    id_empleado: int
    id_proyecto: int
    id_tipo_contrato: int
    inicio_contrato: date
    fin_contrato: date

    class Config:
        orm_mode = True
