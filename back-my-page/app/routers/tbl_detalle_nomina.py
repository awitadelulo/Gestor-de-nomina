from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db

from app.models.tbl_detalle_nomina import tbl_detalle_nomina 
from app.schemas.tbl_detalle_nomina import tbl_detalle_nomina_schema


router = APIRouter(
    prefix="/detalle_nomina",
    tags=["DetalleNomina"]
)

@router.get("/", response_model=List[tbl_detalle_nomina_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_detalle_nomina).all()