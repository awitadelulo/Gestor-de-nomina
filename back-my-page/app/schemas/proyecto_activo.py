from pydantic import BaseModel

class ProyectoActivo(BaseModel):
    id_proyecto: int
    nombre_proyecto: str
    estado: str

    class Config:
        orm_mode = True