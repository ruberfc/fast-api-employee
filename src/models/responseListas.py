
from pydantic import BaseModel
from typing import Optional

from src.models.empleado import Empleado, EmpleadoLogin

class BasicList(BaseModel):
    List: list[Empleado] | list[EmpleadoLogin]