# app/routers/nomina.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.vw_detalle_nomina import vw_detalle_nomina
from app.schemas.vw_nomina import DetalleNominaResponse
from sqlalchemy import func
router = APIRouter(
    prefix="/vw_nomina",
    tags=["vw_nomina"]
)

@router.get("/", response_model=list[DetalleNominaResponse])
def get_detalle_nomina(db: Session = Depends(get_db)):
    resultados = db.query(vw_detalle_nomina).all()
    return resultados

@router.get("/{nombre}", response_model=list[DetalleNominaResponse])
def get_detalle_nomina_por_nombre(nombre: str, db: Session = Depends(get_db)):
    resultados = db.query(vw_detalle_nomina).filter(
        func.lower(vw_detalle_nomina.empleado).like(f"%{nombre.lower()}%")
    ).all()
    return resultados
