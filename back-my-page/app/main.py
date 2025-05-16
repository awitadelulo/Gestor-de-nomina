from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import tbl_estado_proyecto,tbl_detalle_liquidacion,tbl_detalle_nomina,tbl_empleados_proyectos,tbl_empleados,tbl_liquidacion,tbl_nomina,tbl_proyecto,tbl_tipo_contrato
from app.routers import CreateEmpleado,actualizarempleado,eliminar,MostrarEmpleados,proyecto_activo,vw_nomina
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # o ["*"] en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tbl_estado_proyecto.router)
app.include_router(tbl_detalle_liquidacion.router)
app.include_router(tbl_detalle_nomina.router)
app.include_router(tbl_empleados_proyectos.router)
app.include_router(tbl_empleados.router)
app.include_router(tbl_liquidacion.router)
app.include_router(tbl_nomina.router)
app.include_router(tbl_proyecto.router)
app.include_router(tbl_tipo_contrato.router)
app.include_router(CreateEmpleado.router)
app.include_router(actualizarempleado.router)
app.include_router(eliminar.router)
app.include_router(MostrarEmpleados.router)
app.include_router(proyecto_activo.router)
app.include_router(vw_nomina.router)

