from decouple import config
#import pyodbc

def stringConnection() -> str:
    server = config('HOST_NAME')
    database = config('DATA_BASE')
    username = config('USER_NAME')
    password = config('PASSWORD')

    return 'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password


'''
def conecction():

    server = config('HOST_NAME')
    database = config('DATA_BASE')
    username = config('USER_NAME')
    password = config('PASSWORD')

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return cnxn


from pyodbc.pooling import SimpleConnectionPool


# Crear el pool de conexiones
connection_pool = pyodbc.pooling.SimpleConnectionPool(
    min_connections=1,
    max_connections=5,
    timeout=30,
    **{
        "DRIVER": "{SQL Server}",
        "SERVER": config('HOST_NAME'),
        "DATABASE": config('DATA_BASE'),
        "UID": config('USER_NAME'),
        "PWD": config('PASSWORD')
    }
)

# Función para obtener una conexión del pool
def get_connection():
    return connection_pool.getconn()

# Función para devolver la conexión al pool
def return_connection(connection):
    connection_pool.putconn(connection)

'''
