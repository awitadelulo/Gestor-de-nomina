from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db

from app.models.tbl_liquidacion import tbl_liquidacion  
from app.schemas.tbl_liquidacion import tbl_liquidacion_schema


router = APIRouter(
    prefix="/liquidacion",
    tags=["Liquidacion"]
)

@router.get("/", response_model=List[tbl_liquidacion_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_liquidacion).all()