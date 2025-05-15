from fastapi import FastAPI

from app.routers import tbl_estado_proyecto,tbl_detalle_liquidacion,tbl_detalle_nomina,tbl_empleados_proyectos,tbl_empleados,tbl_liquidacion,tbl_nomina,tbl_proyecto,tbl_tipo_contrato

app = FastAPI()

app.include_router(tbl_estado_proyecto.router)
app.include_router(tbl_detalle_liquidacion.router)
app.include_router(tbl_detalle_nomina.router)
app.include_router(tbl_empleados_proyectos.router)
app.include_router(tbl_empleados.router)
app.include_router(tbl_liquidacion.router)
app.include_router(tbl_nomina.router)
app.include_router(tbl_proyecto.router)
app.include_router(tbl_tipo_contrato.router)

