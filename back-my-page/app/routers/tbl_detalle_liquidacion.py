from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db

from app.models.tbl_detalle_liquidacion import tbl_detalle_liquidacion
from app.schemas.tbl_detalle_liquidacion import tbl_detalle_liquidacion_schema


router = APIRouter(
    prefix="/detalle_liquidacion",
    tags=["DetalleLiquidacion"]
)

@router.get("/", response_model=List[tbl_detalle_liquidacion_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_detalle_liquidacion).all()

