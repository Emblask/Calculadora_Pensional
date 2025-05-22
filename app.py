from flask import Flask, render_template, redirect, url_for, flash
from src.controller.usuarios_controller import UsuariosController
from src.routes import register_routes
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_tablas')
def crear():
    try:
        UsuariosController.crear_tabla()
        flash('Tablas creadas exitosamente.')
    except Exception as e:
        flash(f'Error al crear tablas: {e}')
    return redirect(url_for('index'))

# Registrar Blueprints
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
