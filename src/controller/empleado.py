import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.service.empleado  import get_login, get_all_employee, get_employee_by_id, insert_update_employee, delete_employee
from src.models.empleado import EmpleadoLogin, Empleado
from src.models.responseListas import BasicList
from src.models.response import Value, response_Value, response_Custom

routerEmpleado = APIRouter()

@routerEmpleado.get('/login', response_model=EmpleadoLogin, tags=["Empleado"]
    # response_model=Empleado,
    # response_model_include={"IdEmpleado", "Apellidos", "Nombres", "Rol", "Estado", "Usuario"}
)
async def Login(usuario: str, password: str):

    try:
        rpta = get_login(usuario, password)

        if rpta is None:
            #print("vacio")
            resp = response_Custom("No se encontraron resultados", state=2)
            return JSONResponse(resp)

        if isinstance(rpta, EmpleadoLogin):
            #print("Bien")
            return rpta
        
    except Exception as e:
        #print("Fallido")
        #content = {"message": "Error de servidor: "+str(e), "code": 3, state": status.HTTP_500_INTERNAL_SERVER_ERROR }
        #raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error de servidor: "+str(e))

        resp = response_Custom("Error de servidor: "+str(e), 500, 3)
        return JSONResponse(resp, status_code=500)
    
    
@routerEmpleado.get('/List', response_model=BasicList, tags=["Empleado"])
async def Get_All_Employee():
    try:
        rpta = get_all_employee()

        # list_data = [item.dict() for item in rpta]
        # return JSONResponse(content={"List": list_data}, status_code=200)
    
        list_data = [item.dict() for item in rpta]
        return {"List": list_data} 

    except Exception as e:
        resp = response_Custom("Error de servidor: "+str(e), 500, 3)
        return JSONResponse(resp, status_code=500)


@routerEmpleado.get('/{idEmpleado}', response_model=Empleado, tags=["Empleado"])
async def Get_Employee_By_Id(idEmpleado: str):

    try:

        rpta = get_employee_by_id(idEmpleado)

        if rpta is None:
            resp = response_Custom("No se encontraron resultados", state=2)
            return JSONResponse(resp)
        
        if isinstance(rpta, Empleado):
            return rpta

    except Exception as e:
        resp = response_Custom("Error de servidor: "+str(e), 500, 3)
        return JSONResponse(resp, status_code=500)
        

@routerEmpleado.post("/{mode}", response_model=Value, tags=["Empleado"])
async def Insert_Update_Employee(mode: str, empleado: Empleado):

    try:
        rpta = insert_update_employee(mode, empleado)

        if rpta == "empty":
            #raise HTTPException(status_code=404, detail="No se pudo realizar la operación")
            resp = response_Custom("El id no existe", state=2)
            return JSONResponse(resp)
        
        if rpta == "insert":
            resp = response_Value(rpta)
            return resp
        
        if rpta == "update":
            resp = response_Value(rpta)
            return resp
        
    except Exception as e:
        resp = response_Custom("Error de servidor: "+str(e), 500, 3)
        return JSONResponse(resp, status_code=500)

@routerEmpleado.delete("/{idEmpleado}", response_model=Value, tags=["Empleado"])
async def Delete_Employee(idEmpleado: str):

    try:

        rpta = delete_employee(idEmpleado)

        if rpta == "empty":
            # raise HTTPException(status_code=404, detail="No se pudo realizar la operación")
            resp = response_Custom("El id no existe", state=2)
            return JSONResponse(resp)
        
        if rpta == "delete":
            resp = response_Value(rpta)
            return resp
        
    except Exception as e:
        resp = response_Custom("Error de servidor: "+str(e), 500, 3)
        return JSONResponse(resp, status_code=500)