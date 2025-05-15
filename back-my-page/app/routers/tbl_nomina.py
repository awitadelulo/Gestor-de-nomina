from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.tbl_nomina import tbl_nomina 
from app.schemas.tbl_nomina import tbl_nomina_schema


router = APIRouter(
    prefix="/nomina",
    tags=["Nomina"]
)

@router.get("/", response_model=List[tbl_nomina_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_nomina ).all()