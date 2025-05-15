from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.tbl_empleados_proyectos import tbl_empleados_proyectos 
from app.schemas.tbl_empleados_proyectos import tbl_empleados_proyectos_schema

router = APIRouter(
    prefix="/empleados_proyectos",
    tags=["EstadoProyecto"]
)


@router.get("/", response_model=List[tbl_empleados_proyectos_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_empleados_proyectos).all()