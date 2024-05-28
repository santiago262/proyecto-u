from .connection import get_database_connection

def add_data(nombre, E, densidad, costo_por_kg, imagen_url):
    connection = get_database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            INSERT INTO materiales (nombre, E, densidad, costo_por_kg, imagen_url)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, E, densidad, costo_por_kg, imagen_url))
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()