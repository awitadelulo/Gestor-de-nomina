from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db

from app.schemas.mostrar_empleados import EmpleadoResponse

from app.models.tbl_empleados import tbl_empleados
from app.models.tbl_empleados_proyectos import tbl_empleados_proyectos
from app.models.tbl_tipo_contrato import tbl_tipo_contrato
from app.models.tbl_proyecto import tbl_proyecto
from app.models.tbl_estado_proyecto import tlb_estado_proyecto

router = APIRouter(
    prefix="/MostrarEmpleados",
    tags=["MostrarEmpleados"]
)

@router.get("/", response_model=list[EmpleadoResponse])
def get_all_empleados(nombre: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(tbl_empleados)
    if nombre:
        query = query.filter(func.lower(tbl_empleados.nombre).like(f"%{nombre.lower()}%"))
    empleados = query.all()

    empleados_response = []
    for empleado in empleados:
        tipo_contrato = db.query(tbl_tipo_contrato).filter(
            tbl_tipo_contrato.id_tipo_contrato == empleado.id_tipo_contrato
        ).first()

        relaciones = db.query(tbl_empleados_proyectos).filter(
            tbl_empleados_proyectos.id_empleado == empleado.id_empleado
        ).all()

        proyectos_data = []
        for rel in relaciones:
            proyecto = db.query(tbl_proyecto).filter(
                tbl_proyecto.id_proyecto == rel.id_proyecto
            ).first()

            estado = db.query(tlb_estado_proyecto).filter(
                tlb_estado_proyecto.id_estado == proyecto.id_estado
            ).first()

            proyectos_data.append({
                "nombreproyecto": proyecto.nombre_proyecto,
                "iniciocontrato": rel.inicio_contrato,
                "fincontrato": rel.fin_contrato,
                "fechainicio": proyecto.fecha_inicio,
                "fechafin": proyecto.fecha_fin,
                "estadoproyecto": estado.descripcion
            })

        empleados_response.append({
            "id": empleado.id_empleado,
            "nombre": empleado.nombre,
            "apellidos": empleado.apellidos,
            "salariobasico": empleado.salario_basico,
            "fechacontratacion": empleado.fecha_contratacion,
            "tipocontrato": tipo_contrato.descripcion if tipo_contrato else "no definido",
            "proyectos": proyectos_data
        })

    return empleados_response
