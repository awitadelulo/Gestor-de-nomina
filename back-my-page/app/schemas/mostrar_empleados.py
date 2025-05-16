from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ProyectoEmpleado(BaseModel):
    nombreproyecto: str
    iniciocontrato: date
    fincontrato: date
    fechainicio: date
    fechafin: date
    estadoproyecto: str

class EmpleadoResponse(BaseModel):
    id: int
    nombre: str
    apellidos: str
    salariobasico: float
    fechacontratacion: date
    tipocontrato: str
    proyectos: list[ProyectoEmpleado]