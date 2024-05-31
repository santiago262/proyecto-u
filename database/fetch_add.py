# database/fetch_add.py
from connection import get_database_connection

def fetch():
    connection = get_database_connection()
    cursor = connection.cursor()
    

