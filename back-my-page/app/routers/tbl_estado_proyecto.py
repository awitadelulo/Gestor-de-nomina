from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.tbl_estado_proyecto import tlb_estado_proyecto
from app.schemas.tbl_estado_proyecto import tbl_estado_proyecto_schema

router = APIRouter(
    prefix="/estado_proyecto",
    tags=["EstadoProyecto"]
)

@router.get("/", response_model=List[tbl_estado_proyecto_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tlb_estado_proyecto).all()
