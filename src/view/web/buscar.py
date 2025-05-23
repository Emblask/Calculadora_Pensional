from flask import Blueprint, render_template, request, flash
from src.controller.usuarios_controller import UsuariosController
from src.model.pylogic import pension_total

buscar_bp = Blueprint('buscar', __name__)

@buscar_bp.route('/buscar', methods=['GET', 'POST'])
def buscar():
    persona = None
    pension = None
    if request.method == 'POST':
        cedula = request.form['cedula']
        persona = UsuariosController.buscar_usuario(cedula)
        if not persona:
            flash('No se encontró una persona con esa cédula.')
        else:
            salarios = UsuariosController.obtener_salarios(cedula)
            pension = pension_total(
                salarios,
                persona.genero,
                persona.edad,
                persona.semanas_cotizadas,
                persona.numero_hijos
            )
    return render_template('buscar.html', persona=persona, pension=pension)
