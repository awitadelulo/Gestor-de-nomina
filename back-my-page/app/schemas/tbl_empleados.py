from pydantic import BaseModel
from datetime import date
from decimal import Decimal

# tbl_empleados
class tbl_empleados_schema(BaseModel):
    id_empleado: int
    nombre: str
    apellidos: str
    salario_basico: Decimal
    id_tipo_contrato: int
    fecha_contratacion: date

    class Config:
        orm_mode = True

class createEmpleado(BaseModel):
    nombre: str
    apellidos: str
    salario_basico: Decimal
    id_tipo_contrato: int
    fecha_contratacion: date

    class Config:
        orm_mode = True
    