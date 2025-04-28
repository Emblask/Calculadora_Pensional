import psycopg2

class Database:

    def conexion_db(self):
        self.PGHOST='ep-long-cherry-a45as7bw-pooler.us-east-1.aws.neon.tech'
        self.PGDATABASE='neondb'
        self.PGUSER='neondb_owner'
        self.PGPASSWORD='npg_waIM6AZUgBf0'

        self.conexion = psycopg2.connect(host = self.PGHOST, database = self.PGDATABASE, user = self.PGUSER, password = self.PGPASSWORD)
        self.mi_cursor = self.conexion.cursor()

