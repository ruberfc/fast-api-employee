from pydantic import BaseModel
from typing import Optional
from datetime import date

class Empleado(BaseModel):
    IdEmpleado: Optional[str]
    TipoDocumento: Optional[int]
    NumeroDocumento: Optional[str]
    Apellidos: Optional[str]
    Nombres: Optional[str]
    Sexo: Optional[int]
    FechaNacimiento: Optional[str]
    Puesto: Optional[int]
    Rol: Optional[int]
    Estado: Optional[int]
    Telefono: Optional[str]
    Celular: Optional[str]
    Email: Optional[str]
    Direccion: Optional[str]
    Usuario: Optional[str]
    Clave: Optional[str]
    Sistema: Optional[bool]
    Huella: Optional[str]

class EmpleadoLogin(BaseModel):
    IdEmpleado: Optional[str]
    Apellidos: Optional[str]
    Nombres: Optional[str]
    Rol: Optional[int]
    Estado: Optional[int]
    Usuario: Optional[str]


