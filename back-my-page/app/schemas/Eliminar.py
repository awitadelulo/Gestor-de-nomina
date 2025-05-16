from pydantic import BaseModel

class Eliminar(BaseModel):
    nombre: str
    apellidos: str
    
    class Config:
        orm_mode = True