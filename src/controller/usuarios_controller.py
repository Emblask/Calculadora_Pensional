import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig

class UsuariosController:
    def crear_tabla():
        cursor = UsuariosController.obtener_cursos()

        with open("sql/crear_usuarios.sql", "r") as archivo:
            consulta = archivo.read()
        
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = UsuariosController.obtener_cursos()

        with open("sql/borrar_usuarios.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    def obtener_cursos():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor

if __name__ == "__main__":
    UsuariosController.borrar_tabla()

