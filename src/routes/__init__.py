from .insertar import insertar_bp
from .buscar import buscar_bp
from .modificar import modificar_bp

def register_routes(app):
    app.register_blueprint(insertar_bp)
    app.register_blueprint(buscar_bp)
    app.register_blueprint(modificar_bp)
