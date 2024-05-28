# database.py
import mysql.connector

def get_database_connection():
    # Define la URL de conexión
    url = "mysql://root:MSbxkDyFyVJuVrIyUziNvPtNneDkVaZQ@roundhouse.proxy.rlwy.net:32513/railway"
    
    # Parsea la URL para obtener los componentes de conexión
    url_components = {
        'host': 'roundhouse.proxy.rlwy.net',
        'port': 32513,
        'user': 'root',
        'password': 'MSbxkDyFyVJuVrIyUziNvPtNneDkVaZQ',
        'database': 'railway'
    }

    # Crea una conexión utilizando los componentes obtenidos
    connection = mysql.connector.connect(**url_components)
    
    return connection
