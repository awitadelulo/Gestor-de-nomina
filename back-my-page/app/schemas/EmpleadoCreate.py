from pydantic import BaseModel
from datetime import date

class EmpleadoCreate(BaseModel):
    nombre: str
    apellidos: str
    salario: float
    tipoContrato: int
    fechaContratacion: date
    proyecto: int
    tipoContratoProyecto: int
    inicioContrato: date
    finContrato: date
    
    class Config:
        orm_mode = True