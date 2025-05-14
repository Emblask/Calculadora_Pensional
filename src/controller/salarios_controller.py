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

        consulta = f"insert into salarios values ('{salarios.cedula}', '{salarios.salario_1}', '{salarios.salario_2}', '{salarios.salario_3}', '{salarios.salario_4}', '{salarios.salario_5}', '{salarios.salario_6}', '{salarios.salario_7}', '{salarios.salario_8}', '{salarios.salario_9}', '{salarios.salario_10}')"
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar_salarios(cedula) -> Salarios:
        cursor = SalariosController.obtener_cursor()

        consulta = f"select * from salarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        fila = cursor.fetchone()

        if fila is None:
            return None
        
        resultado = Salarios(cedula = int(fila[0]), salario_1 = int(fila[1]), salario_2 = int(fila[2]), salario_3 = int(fila[3]), salario_4 = int(fila[4]), salario_5 = int(fila[5]), salario_6 = int(fila[6]), salario_7 = int(fila[7]), salario_8 = int(fila[8]), salario_9 = int(fila[9]), salario_10 = int(fila[10]))
        return resultado

    def obtener_cursor():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor
    
    
if __name__ == "__main__":
    SalariosController.crear_tabla_salarios()
    

    
