import unittest
import sys

sys.path.append ("src")

from model.usuario import Usuario

from controller.usuarios_controller import UsuariosController

class TestTarjeta(unittest.TestCase):

    def setUpClass():
        UsuariosController.borrar_tabla()
        UsuariosController.crear_tabla()

    def test_insert_1(self):
        usuario = Usuario(  cedula = 1022145818,
                            nombre = "David",
                            apellido = "Hernandez",
                            edad = 71,
                            genero = "Masculino")
        
        UsuariosController.insertar(usuario)
        usuario_buscado = UsuariosController.buscar_usuario(usuario.cedula)
        self.assertTrue(usuario_buscado.EsIgual(usuario))


if __name__ == "__main__":
    unittest.main()