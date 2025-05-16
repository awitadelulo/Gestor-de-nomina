from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tbl_empleados import tbl_empleados
from app.models.tbl_empleados_proyectos import tbl_empleados_proyectos
from app.schemas.EmpleadoCreate import EmpleadoCreate
from datetime import datetime

router = APIRouter(
    prefix="/CrearEmpleado",
    tags=["CrearEmpleado"]
)

@router.post("/")
def crear_empleado(data:EmpleadoCreate,db: Session = Depends(get_db)):
    # 1. Crear el empleado
    nuevo_empleado = tbl_empleados(
        nombre=data.nombre,
        apellidos=data.apellidos,
        salario_basico=data.salario,
        id_tipo_contrato=data.tipoContrato,
        fecha_contratacion=data.fechaContratacion
    )
    db.add(nuevo_empleado)
    db.commit()
    db.refresh(nuevo_empleado)

    # 2. Asignarlo a un proyecto
    asignacion = tbl_empleados_proyectos(
        id_empleado=nuevo_empleado.id_empleado,
        id_proyecto=data.proyecto,
        id_tipo_contrato=data.tipoContratoProyecto,
        inicio_contrato=data.inicioContrato,
        fin_contrato=data.finContrato
    )
    db.add(asignacion)
    db.commit()

    return {"mensaje": "Empleado creado exitosamente", "id_empleado": nuevo_empleado.id_empleado}