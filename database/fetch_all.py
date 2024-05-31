# database/fetch_all.py

from .connection import get_database_connection
from .material import Material

def fetch_all_records():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)  # Configura el cursor para devolver los resultados como diccionarios
    cursor.execute("SELECT * FROM materiales")
    rows = cursor.fetchall()
    connection.close()

    # Convertir los registros en objetos Material
    

    return rows
