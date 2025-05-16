
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.proyectos_activos import vw_proyectos_activos
from app.schemas.proyecto_activo import ProyectoActivo

router = APIRouter(
    prefix="/proyectos-activos",
    tags=["Proyectos Activos"]
)

@router.get("/", response_model=list[ProyectoActivo])
def get_proyectos_activos(db: Session = Depends(get_db)):
    return db.query(vw_proyectos_activos).all()