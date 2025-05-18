from flask import Flask, render_template, request, redirect, url_for, flash
from SecretConfig import PGHOST, PGDATABASE, PGUSER, PGPASSWORD, PGPORT
import psycopg2
from src.model.pylogic import pension_total
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def conectar():
    return psycopg2.connect(
        database=PGDATABASE,
        user=PGUSER,
        password=PGPASSWORD,
        host=PGHOST,
        port=PGPORT
    )

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def leer_sql(nombre_archivo):
    ruta = os.path.join(BASE_DIR, "sql", f"{nombre_archivo}.sql")
    print("Intentando abrir archivo:", ruta)
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def ejecutar_sql(nombre_archivo, parametros=None, fetchone=False):
    conn = conectar()
    cur = conn.cursor()
    query = leer_sql(nombre_archivo)
    cur.execute(query, parametros or ())
    resultado = None
    if fetchone:
        resultado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return resultado

def crear_usuarios():
    ejecutar_sql("crear_usuarios")

def insertar_usuario(datos):
    parametros = (
        datos['cedula'],
        datos['nombre'],
        datos['apellido'],
        int(datos['edad']),
        datos['genero'],
        datos['numero_hijos'],
        datos['semanas_cotizadas'],
        *datos['salarios'],  # 10 salarios
    )
    ejecutar_sql("insertar_usuario", parametros)

def buscar_usuario(cedula):
    return ejecutar_sql("buscar_usuario", (cedula,), fetchone=True)

def modificar_usuario(cedula, datos):
    parametros = (
        datos['nombre'],
        datos['apellido'],
        int(datos['edad']),
        datos['genero'],
        datos['numero_hijos'],
        datos['semanas_cotizadas'],
        *datos['salarios'],
        cedula
    )
    ejecutar_sql("modificar_usuario", parametros)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_tablas')
def crear():
    try:
        crear_usuarios()
        flash('Tablas creadas exitosamente.')
    except Exception as e:
        flash(f'Error al crear tablas: {e}')
    return redirect(url_for('index'))

@app.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        try:
            salarios = [float(request.form[f'salario_{i+1}']) for i in range(10)]
            datos = {
                'cedula': request.form['cedula'],
                'nombre': request.form['nombre'],
                'apellido': request.form['apellido'],
                'edad': request.form['edad'],
                'genero': request.form['genero'],
                'numero_hijos': int(request.form['numero_hijos']),
                'semanas_cotizadas': int(request.form['semanas_cotizadas']),
                'salarios': salarios
            }
            insertar_usuario(datos)
            pension = pension_total(
                datos['salarios'],
                datos['genero'],
                int(datos['edad']),
                datos['semanas_cotizadas'],
                datos['numero_hijos']
            )
            flash(f'Datos insertados con éxito. Pensión calculada: ${float(pension):.2f}')

        except Exception as e:
            flash(f'Error al insertar: {str(e)}')
        return redirect(url_for('index'))
    return render_template('insertar.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    persona = None
    pension = None
    if request.method == 'POST':
        cedula = request.form['cedula']
        persona = buscar_usuario(cedula)
        if not persona:
            flash('No se encontró una persona con esa cédula.')
        else:
            # Convertir datos necesarios a int y float para el cálculo
            edad = int(persona[3])
            genero = persona[4]
            numero_hijos = int(persona[5])
            semanas_cotizadas = int(persona[6])
            salarios = [float(persona[i]) for i in range(7, 17)]  # 10 salarios

            pension = pension_total(salarios, genero, edad, semanas_cotizadas, numero_hijos)

    return render_template('buscar.html', persona=persona, pension=pension)


@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    if request.method == 'POST':
        try:
            cedula = request.form['cedula']
            salarios = [float(request.form[f'salario_{i+1}']) for i in range(10)]
            nuevos_datos = {
                'nombre': request.form['nombre'],
                'apellido': request.form['apellido'],
                'edad': request.form['edad'],
                'genero': request.form['genero'],
                'numero_hijos': int(request.form['numero_hijos']),
                'semanas_cotizadas': int(request.form['semanas_cotizadas']),
                'salarios': salarios
            }
            modificar_usuario(cedula, nuevos_datos)
            pension = pension_total(
                nuevos_datos['salarios'],
                nuevos_datos['genero'],
                int(nuevos_datos['edad']),
                nuevos_datos['semanas_cotizadas'],
                nuevos_datos['numero_hijos']
            )
            flash(f'Datos modificados con éxito. Pensión calculada: ${pension:.2f}')
        except Exception as e:
            flash(f'Error al modificar: {str(e)}')
        return redirect(url_for('index'))
    return render_template('modificar.html')

if __name__ == '__main__':
    app.run(debug=True)
