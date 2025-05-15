from pydantic import BaseModel

class tbl_estado_proyecto_schema(BaseModel):
    id_estado:int
    descripcion:str

    class Config:
        orm_mode = True