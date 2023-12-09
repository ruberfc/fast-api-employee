from fastapi import FastAPI
from src.controller.empleado import routerEmpleado

app = FastAPI()

base_path = "/api/v1/empleado"
app.include_router(routerEmpleado, prefix=base_path)

@app.get('/')
def index():
    return {"Api-Rest": "Prueba", "version": "1.0"}


    
