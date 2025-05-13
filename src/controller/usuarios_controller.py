import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig
from model.usuario import Usuario

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
    
    def insertar(usuario: Usuario):
        cursor = UsuariosController.obtener_cursos()

        consulta = f"insert into usuarios values ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}', '{usuario.edad}', '{usuario.genero}')"
        cursor.execute(consulta)
        cursor.connection.commit()
    
    def buscar_usuario(cedula) -> Usuario:
        cursor = UsuariosController.obtener_cursos()

        consulta = f"select * from usuarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        fila = cursor.fetchone()
        resultado = Usuario(cedula = int(fila[0]), nombre = fila[1], apellido = fila[2], edad = int(fila[3]), genero = fila[4])
        return resultado

    def obtener_cursos():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor


