# app/schemas/nomina.py

from pydantic import BaseModel

class DetalleNominaResponse(BaseModel):
    id_nomina: int
    id_empleado: int
    empleado: str
    concepto: str
    valor: float

    class Config:
        orm_mode = True