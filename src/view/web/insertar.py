from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.controller.usuarios_controller import UsuariosController
from src.model.usuario import Usuario
from src.model.pylogic import pension_total

insertar_bp = Blueprint('insertar', __name__)

@insertar_bp.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        try:
            salarios = [float(request.form[f'salario_{i+1}']) for i in range(10)]
            usuario = Usuario(
                cedula=int(request.form['cedula']),
                nombre=request.form['nombre'],
                apellido=request.form['apellido'],
                edad=int(request.form['edad']),
                genero=request.form['genero'],
                numero_hijos=int(request.form['numero_hijos']),
                semanas_cotizadas=int(request.form['semanas_cotizadas']),
                salario_1=salarios[0], salario_2=salarios[1], salario_3=salarios[2],
                salario_4=salarios[3], salario_5=salarios[4], salario_6=salarios[5],
                salario_7=salarios[6], salario_8=salarios[7], salario_9=salarios[8],
                salario_10=salarios[9]
            )
            UsuariosController.insertar(usuario)
            pension = pension_total(
                salarios,
                usuario.genero,
                usuario.edad,
                usuario.semanas_cotizadas,
                usuario.numero_hijos
            )
            flash(f'Datos insertados con éxito. Pensión calculada: ${pension:.2f}')
        except Exception as e:
            flash(f'Error al insertar: {str(e)}')
        return redirect(url_for('index'))
    return render_template('insertar.html')
