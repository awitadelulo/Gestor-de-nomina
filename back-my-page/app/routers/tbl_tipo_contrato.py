from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db

from app.models.tbl_tipo_contrato import tbl_tipo_contrato 
from app.schemas.tbl_tipo_contrato import tbl_tipo_contrato_schema


router = APIRouter(
    prefix="/tipo_contrato",
    tags=["TipoContrato"]
)

@router.get("/", response_model=List[tbl_tipo_contrato_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_tipo_contrato).all()