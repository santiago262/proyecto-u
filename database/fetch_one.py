# database/fetch_one.py

from .connection import get_database_connection
import mysql.connector
from mysql.connector import Error

def fetch_one_record(id):
    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM materiales WHERE id = %s", (id,))
        row = cursor.fetchone()
    except Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        row = None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")
    
    return row
