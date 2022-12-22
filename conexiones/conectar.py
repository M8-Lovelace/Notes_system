# Instalamos e importamos la librería para manipular la base de datos
import mysql.connector
from mysql.connector import errorcode

# DDL => Modifica la estructura de la base de datos.
# DML => Inserta, modifica, trae, elimina los datos de la base de datos.

# Configuración para la conexión
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'notas',
}

def conexion():
    # Generamos la conexión
    try:
        database = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")

    # Creamos el cursor para manipulación de la base de datos
    cursor = database.cursor(buffered=True)

    return [database, cursor]