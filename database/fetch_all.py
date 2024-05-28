# database/fetch_all.py

from .connection import get_database_connection
from .material import Material
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
    
    return rows
