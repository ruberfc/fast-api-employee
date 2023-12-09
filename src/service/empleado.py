import pyodbc
from typing import Optional
from src.database.conecction import  stringConnection
from src.models.empleado import EmpleadoLogin, Empleado

connection = stringConnection()


def get_login(usuario: str, password: str) -> Optional[EmpleadoLogin]:
    
    try:
        with pyodbc.connect(connection) as conn:
            cursor = conn.cursor()

            try:

                query = """SELECT TOP 1 IdEmpleado, Apellidos, Nombres, Rol, Estado, Usuario FROM EmpleadoTB WHERE Usuario = ? AND Clave = ? AND Estado = 1"""
                cursor.execute(query, (usuario, password))
                row = cursor.fetchone()

                if row is None:
                    return None
                else:
                    empleado = EmpleadoLogin(
                        IdEmpleado=row[0],
                        Apellidos=row[1],
                        Nombres=row[2],
                        Rol=row[3],
                        Estado=row[4],
                        Usuario=row[5],
                    )
                    return empleado
                
            finally:
                if cursor:
                    cursor.close()
    except Exception as e:
        raise e


def get_all_employee() -> list[Empleado]:
    
    try:

        with pyodbc.connect(connection) as conn:
            cursor = conn.cursor()

            try:
                # query = """SELECT * FROM EmpleadoTB WHERE IdEmpleado = 'EM0009'""" 
                query = """SELECT * FROM EmpleadoTB"""    
                cursor.execute(query)
                rows = cursor.fetchall()

                empleados = []

                for row in rows:
                    emp = Empleado(
                        #IdEmpleado = row.IdEmpleado,
                        IdEmpleado = row[0],
                        TipoDocumento = row[1],
                        NumeroDocumento = row[2],
                        Apellidos = row[3],
                        Nombres = row[4],
                        Sexo = row[5],
                        FechaNacimiento = row[6],
                        Puesto = row[7],
                        Rol = row[8],
                        Estado = row[9],
                        Telefono = row[10],
                        Celular = row[11],
                        Email = row[12],
                        Direccion = row[13],
                        Usuario = row[14],
                        Clave = row[15],
                        Sistema = row[16],
                        Huella = row[17]
                    )

                    empleados.append(emp)

                return empleados
            
            finally:
                if cursor:
                    cursor.close()

    except Exception as e:
        raise e


def get_employee_by_id(id: str) -> Optional[Empleado]:

    try:

        with pyodbc.connect(connection) as conn:
            cursor = conn.cursor()

            try:
                query = """SELECT TOP 1 IdEmpleado, TipoDocumento, NumeroDocumento, Apellidos, Nombres, Sexo,
                        FechaNacimiento, Puesto, Rol, Estado, Telefono, Celular,
                        Email, Direccion, Usuario, Clave, Sistema, Huella 
                        FROM EmpleadoTB WHERE IdEmpleado = ?"""
                cursor.execute(query, (id,))
                row = cursor.fetchone()

                if row is None:
                    return None
                else:
                    emp = Empleado(
                        IdEmpleado = row[0], 
                        TipoDocumento = row[1], 
                        NumeroDocumento = row[2], 
                        Apellidos = row[3], 
                        Nombres = row[4], 
                        Sexo = row[5],
                        FechaNacimiento = row[6], 
                        Puesto = row[7], 
                        Rol = row[8], 
                        Estado = row[9], 
                        Telefono = row[10], 
                        Celular = row[11],
                        Email = row[12], 
                        Direccion = row[13], 
                        Usuario = row[14], 
                        Clave = row[15], 
                        Sistema = row[16], 
                        Huella = row[17]
                    )
                    return emp
                
            finally:
                if cursor:
                    cursor.close()

    except Exception as e:
        raise e


def insert_update_employee(mode: str, emp: Empleado) -> str:  
    
    try:

        with pyodbc.connect(connection) as conn:
            cursor = conn.cursor()

            try:

                if mode == "INSERT":
                    query = """INSERT INTO EmpleadoTB 
                    (IdEmpleado, TipoDocumento, NumeroDocumento, Apellidos, Nombres, Sexo, FechaNacimiento, Puesto, Rol, 
                    Estado, Telefono, Celular, Email, Direccion, Usuario, Clave, Sistema, Huella) 
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                    cursor.execute(query, (
                        emp.IdEmpleado, emp.TipoDocumento, emp.NumeroDocumento, emp.Apellidos, emp.Nombres, emp.Sexo,
                        emp.FechaNacimiento, emp.Puesto, emp.Rol, emp.Estado, emp.Telefono, emp.Celular,
                        emp.Email, emp.Direccion, emp.Usuario, emp.Clave, emp.Sistema, emp.Huella
                    ))

                    if cursor.rowcount > 0:
                        cursor.commit()
                        return "insert"
                    else:
                        cursor.rollback()
                        return "empty"
                    
                if mode == "UPDATE":
                    query = """UPDATE EmpleadoTB SET 
                    TipoDocumento = ?, NumeroDocumento = ?, Apellidos = ?, Nombres = ?, Sexo = ?, FechaNacimiento = ?,
                    Puesto = ?, Rol = ?, Estado = ?, Telefono = ?, Celular = ?, Email = ?,
                    Direccion = ?, Usuario = ?, Clave = ?, Sistema = ?, Huella = ?
                    WHERE IdEmpleado = ?"""
                    cursor.execute(query, (
                        emp.TipoDocumento, emp.NumeroDocumento, emp.Apellidos, emp.Nombres, emp.Sexo, emp.FechaNacimiento,
                        emp.Puesto, emp.Rol, emp.Estado, emp.Telefono,emp.Celular, emp.Email,
                        emp.Direccion, emp.Usuario, emp.Clave, emp.Sistema, emp.Huella, emp.IdEmpleado
                    ))

                    if cursor.rowcount > 0:
                        cursor.commit()
                        return "update"
                    else:
                        cursor.rollback()
                        return "empty"
                    
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                if cursor:
                    cursor.close()

    except Exception as e:
        raise e


def delete_employee(id: str) -> str:
    
    try:

        with pyodbc.connect(connection) as conn:
            cursor = conn.cursor()
            
            try:

                query = """DELETE FROM EmpleadoTB WHERE IdEmpleado = ?"""
                cursor.execute(query, (id,))

                if cursor.rowcount > 0:
                    conn.commit()
                    return "delete"
                else:
                    conn.rollback()
                    return "empty"

            except Exception as e:
                conn.rollback()
                raise e
            finally:
                if cursor:
                    cursor.close()

    except Exception as e:
        raise e
    


'''
def get_login(usuario: str, password: str) -> Optional[EmpleadoLogin]:

    connection = conecction()
    cursor = connection.cursor()
    # cursor = conecction().cursor()

    try:
    
        query = """SELECT TOP 1 IdEmpleado, Apellidos, Nombres, Rol, Estado, Usuario FROM EmpleadoTB WHERE Usuario = ? AND Clave = ? AND Estado = 1"""
        cursor.execute(query, (usuario, password))
        row = cursor.fetchone()

        if row is None:
            return None
        else:
            empleado = EmpleadoLogin(
                IdEmpleado = row[0],
                Apellidos = row[1],
                Nombres = row[2],
                Rol = row[3],
                Estado = row[4],
                Usuario = row[5],
            )
            return empleado
    except Exception as e:
        raise e 
    finally:
        cursor.close()
        connection.close()

'''

'''
def get_empoyed_by_id_example(id: str):
    try:
        cursor = conecction().cursor()
        cursor.execute("select * from EmpleadoTB where IdEmpleado = ?", (id,))

        row_headers = [x[0] for x in cursor.description]
        rows = cursor.fetchall()

        json_data = []
        for row in rows:
            json_data.append(dict(zip(row_headers, row)))

        return json_data

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        conecction().close()
'''
