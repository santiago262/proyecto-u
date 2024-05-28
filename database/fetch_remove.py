
# database/delete_record.py

from .connection import get_database_connection
import mysql.connector
from mysql.connector import Error

def delete_record(id):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        data=connection.cursor()
        data.execute("SELECT * FROM materiales WHERE id = %s", (id,))
        fact= data.fetchone()
        cursor.execute("DELETE FROM materiales WHERE id = %s", (id,))
        connection.commit() 
        print(f"Registro con id {id} eliminado exitosamente.")
    except Error as e:
        print(f"Error al intentar eliminar el registro: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")
    return f"el material: {fact.nombre} a sido iliminado"

