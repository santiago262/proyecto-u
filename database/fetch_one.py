from .connection import get_database_connection

def fetch_one_records(id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM materiales WHERE id = {id}")
    rows = cursor.fetchall()
    connection.close()
    return rows