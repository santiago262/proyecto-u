# database/fetch_all.py

from .connection import get_database_connection
from .material import Material
<<<<<<< HEAD

def fetch_all_records():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)  # Configura el cursor para devolver los resultados como diccionarios
    cursor.execute("SELECT * FROM materiales")
    rows = cursor.fetchall()
    connection.close()

    # Convertir los registros en objetos Material
    

=======
import mysql.connector
from mysql.connector import Error

def fetch_all_records():
    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)  # Configura el cursor para devolver los resultados como diccionarios
        cursor.execute("SELECT * FROM materiales")
        rows = cursor.fetchall()
    except Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        rows = []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")
    
>>>>>>> a9c76ab1e6dedc8b01e9d0500388a34a19bceccb
    return rows
