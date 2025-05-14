import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig
from model.salarios import Salarios

class SalariosController:
    
    def crear_tabla_salarios():
        cursor = SalariosController.obtener_cursor()

        with open("sql/crear_salarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
    
    def borrar_tabla_salarios():
        cursor = SalariosController.obtener_cursor()

        with open("sql/borrar_salarios.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def insertar_datos_salarios(salarios: Salarios):
        cursor = SalariosController.obtener_cursor()

        consulta = f"insert into salarios values ('{salarios.lista_salarios[0]}', '{salarios.lista_salarios[1]}', '{salarios.lista_salarios[2]}', '{salarios.lista_salarios[3]}', '{salarios.lista_salarios[4]}', '{salarios.lista_salarios[5]}', '{salarios.lista_salarios[6]}', '{salarios.lista_salarios[7]}', '{salarios.lista_salarios[8]}', '{salarios.lista_salarios[9]}')"
        cursor.execute(consulta)
        cursor.connection.commit()

    def obtener_cursor():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor
    
    
if __name__ == "__main__":
    SalariosController.crear_tabla_salarios()
    

    
