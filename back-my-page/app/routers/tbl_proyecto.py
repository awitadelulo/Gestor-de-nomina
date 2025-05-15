from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.tbl_proyecto import tbl_proyecto
from app.schemas.tbl_proyecto import tbl_proyecto_schema


router = APIRouter(
    prefix="/proyecto",
    tags=["Proyecto"]
)

@router.get("/", response_model=List[tbl_proyecto_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_proyecto).all()
