from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tbl_empleados import tbl_empleados
from app.models.tbl_tipo_contrato import tbl_tipo_contrato  # <-- importa el modelo correcto
from app.schemas.actualizar_empleado import EmpleadoActualizar
from datetime import datetime

router = APIRouter(
    prefix="/ActualizarEmpleado",
    tags=["ActualizarEmpleado"]
)

@router.put("/")
def actualizar_empleado(data: EmpleadoActualizar, db: Session = Depends(get_db)):
    # 1. Buscar el empleado existente por nombre (aunque idealmente usar id_empleado)
    empleado = db.query(tbl_empleados).filter(tbl_empleados.nombre == data.nombre).first()

    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    # 2. Validar que el tipo de contrato existe
    contrato = db.query(tbl_tipo_contrato).filter(tbl_tipo_contrato.id_tipo_contrato == data.tipoContrato).first()
    if not contrato:
        raise HTTPException(status_code=400, detail=f"Tipo de contrato {data.tipoContrato} no existe")

    # 3. Actualizar datos del empleado
    empleado.nombre = data.nombre
    empleado.apellidos = data.apellidos
    empleado.salario_basico = data.salario
    empleado.id_tipo_contrato = data.tipoContrato
    empleado.fecha_contratacion = data.fechaContratacion

    db.commit()

    return {"mensaje": "Empleado actualizado correctamente"}
