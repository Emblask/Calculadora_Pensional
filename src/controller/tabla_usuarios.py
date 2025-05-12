import sys
import psycopg2

sys.path.append("src")
sys.path.append(".")

import SecretConfig

class TablaUsuarios:
    def crear_tabla():
        cursor = TablaUsuarios.obtener_cursos()
        

    def obtener_cursos():
        conection = psycopg2.connect(database = SecretConfig.PGDATABASE, user = SecretConfig.PGUSER, password = SecretConfig.PGPASSWORD, host = SecretConfig.PGHOST, port = SecretConfig.PGPORT)
        cursor = conection.cursor()
        return cursor

