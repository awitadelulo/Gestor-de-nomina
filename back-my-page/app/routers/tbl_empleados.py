from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db

from app.models.tbl_empleados import  tbl_empleados
from app.schemas.tbl_empleados import tbl_empleados_schema


router = APIRouter(
    prefix="/empleados",
    tags=["Empleados"]
)

@router.get("/", response_model=List[tbl_empleados_schema])
def get_all(db: Session = Depends(get_db)):
    return db.query(tbl_empleados).all()