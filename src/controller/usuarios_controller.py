import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig
from src.model.usuario import Usuario

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

        consulta = f"""insert into usuarios values ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}', '{usuario.edad}',
                                                    '{usuario.genero}', '{usuario.numero_hijos}', '{usuario.semanas_cotizadas}',
                                                    '{usuario.salario_1}', '{usuario.salario_2}', '{usuario.salario_3}',
                                                    '{usuario.salario_4}', '{usuario.salario_5}', '{usuario.salario_6}',
                                                    '{usuario.salario_7}', '{usuario.salario_8}', '{usuario.salario_9}', '{usuario.salario_10}')"""
        cursor.execute(consulta)
        cursor.connection.commit()
    
    def eliminar(cedula: int):
        cursor = UsuariosController.obtener_cursos()

        consulta = f"delete from usuarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        cursor.connection.commit()
        return cursor.rowcount
    
    def buscar_usuario(cedula) -> Usuario:
        cursor = UsuariosController.obtener_cursos()

        consulta = f"select * from usuarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        fila = cursor.fetchone()

        if fila is None:
            return None
        
        resultado = Usuario(cedula = int(fila[0]), nombre = fila[1], apellido = fila[2], edad = int(fila[3]), genero = fila[4],
                            numero_hijos = int(fila[5]), semanas_cotizadas = int(fila[6]), salario_1 = int(fila[7]), salario_2 = int(fila[8]), salario_3 = int(fila[9]),
                            salario_4 = int(fila[10]), salario_5 = int(fila[11]), salario_6 = int(fila[12]), salario_7 = int(fila[13]),
                            salario_8 = int(fila[14]), salario_9 = int(fila[15]), salario_10 = int(fila[16]))
        return resultado
    

    @staticmethod
    def actualizar(usuario: Usuario):
        cursor = UsuariosController.obtener_cursos()
        
        consulta = """UPDATE usuarios SET 
                    nombre = %s, 
                    apellido = %s, 
                    edad = %s, 
                    genero = %s, 
                    numero_hijos = %s, 
                    semanas_cotizadas = %s,
                    salario_1 = %s, salario_2 = %s, salario_3 = %s,
                    salario_4 = %s, salario_5 = %s, salario_6 = %s,
                    salario_7 = %s, salario_8 = %s, salario_9 = %s, salario_10 = %s
                    WHERE cedula = %s"""
        
        parametros = (
            usuario.nombre, usuario.apellido, usuario.edad, usuario.genero,
            usuario.numero_hijos, usuario.semanas_cotizadas,
            usuario.salario_1, usuario.salario_2, usuario.salario_3,
            usuario.salario_4, usuario.salario_5, usuario.salario_6,
            usuario.salario_7, usuario.salario_8, usuario.salario_9, usuario.salario_10,
            str(usuario.cedula)
        )
        
        cursor.execute(consulta, parametros)
        cursor.connection.commit()
        return cursor.rowcount
    
    def obtener_salarios(cedula):
        resultado = []
        cursor = UsuariosController.obtener_cursos()

        consulta = f"select * from usuarios where cedula = '{cedula}'"
        cursor.execute(consulta)
        fila = cursor.fetchone()

        if fila is None:
            return None
        
        resultado.extend(   [int(fila[7]), int(fila[8]), int(fila[9]), int(fila[10]), int(fila[11]),
                            int(fila[12]), int(fila[13]), int(fila[14]), int(fila[15]), int(fila[16])])
        return resultado

    def obtener_cursos():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor

