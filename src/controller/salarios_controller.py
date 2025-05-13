import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig

class Controlar_usuarios:
    
    def crear_tabla():
        cursor = Controlar_usuarios.obtener_cursor()
        with open("sql/crear_usuarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    
    def obtener_cursor():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor
