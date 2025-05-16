from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tbl_empleados import tbl_empleados
from app.schemas.Eliminar import Eliminar

router = APIRouter(
    prefix="/Eliminar",
    tags=["Eliminar"]
)

@router.post("/eliminar")
def eliminar(data: Eliminar, db: Session = Depends(get_db)):
    empleado = db.query(tbl_empleados).filter(
        tbl_empleados.nombre == data.nombre,
        tbl_empleados.apellidos == data.apellidos
    ).first()

    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    db.delete(empleado)
    db.commit()

    return {"mensaje": "Empleado eliminado correctamente"}

