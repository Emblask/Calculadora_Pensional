import psycopg2

class Database:

    def conexion_db(self):
        self.PGHOST='ep-long-cherry-a45as7bw-pooler.us-east-1.aws.neon.tech'
        self.PGDATABASE='neondb'
        self.PGUSER='neondb_owner'
        self.PGPASSWORD='npg_waIM6AZUgBf0'

        self.conexion = psycopg2.connect(host = self.PGHOST, database = self.PGDATABASE, user = self.PGUSER, password = self.PGPASSWORD)
        self.mi_cursor = self.conexion.cursor()

    def crear_tabla_usuarios(self):
        self.mi_cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                            Cedula INTEGER PRIMARY KEY,
                            Nombre TEXT NOT NULL,
                            Edad SMALLINT NOT NULL,
                            Semanas_Cotizadas INTEGER NOT NULL
                            )""")
        self.conexion.commit() 


if __name__ == "__main__":
    base_datos = Database()
    base_datos.conexion_db()