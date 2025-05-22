from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.controller.usuarios_controller import UsuariosController
from src.model.usuario import Usuario
from src.model.pylogic import pension_total

modificar_bp = Blueprint('modificar', __name__)

@modificar_bp.route('/modificar', methods=['GET', 'POST'])
def modificar():
    if request.method == 'POST':
        try:
            cedula = int(request.form['cedula'])
            usuario_existente = UsuariosController.buscar_usuario(cedula)
            if not usuario_existente:
                flash('No existe ningún usuario con esa cédula.', 'error')
                return redirect(url_for('modificar.modificar'))

            salarios = [float(request.form[f'salario_{i+1}']) for i in range(10)]
            usuario_actualizado = Usuario(
                cedula=cedula,
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

            filas_afectadas = UsuariosController.actualizar(usuario_actualizado)
            if filas_afectadas == 0:
                flash('No se modificó ningún registro.', 'warning')
            else:
                pension = pension_total(
                    salarios,
                    usuario_actualizado.genero,
                    usuario_actualizado.edad,
                    usuario_actualizado.semanas_cotizadas,
                    usuario_actualizado.numero_hijos
                )
                flash(f'Datos modificados con éxito. Pensión: ${pension:.2f}', 'success')

        except Exception as e:
            flash(f'Error al modificar: {str(e)}', 'error')
        return redirect(url_for('index'))
    return render_template('modificar.html')
