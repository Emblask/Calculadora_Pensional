import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig

class Controlar_Salarios:
    
    def crear_tabla_salarios():
        cursor = Controlar_Salarios.obtener_cursor()
        with open("sql/crear_salarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    
    def obtener_cursor():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor
    
    def borrar_tabla_salarios():
        cursor = Controlar_Salarios.obtener_cursor()
        with open("sql/borrar_salarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def insertar_datos_salarios():
        ...

if __name__ == "__main__":
    Controlar_Salarios.crear_tabla_salarios()
