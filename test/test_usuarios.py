import unittest
import sys

sys.path.append ("src")

from model.usuario import Usuario

from controller.usuarios_controller import UsuariosController

class TestTarjeta(unittest.TestCase):

    def setUpClass():
        UsuariosController.borrar_tabla()
        UsuariosController.crear_tabla()

    def test_insertar_normal_1(self):
        usuario = Usuario(  cedula = 1022145818,
                            nombre = "David",
                            apellido = "Hernandez",
                            edad = 71,
                            genero = "Masculino",
                            numero_hijos = 1)
        
        UsuariosController.insertar(usuario)
        usuario_buscado = UsuariosController.buscar_usuario(usuario.cedula)
        self.assertTrue(usuario_buscado.EsIgual(usuario))
    
    def test_insertar_error_2(self):
        usuario =  Usuario( cedula = 43669647,
                            nombre = "Isabel",
                            apellido = "Trespalacios",
                            edad = 68,
                            genero = "Femenino",
                            numero_hijos = 2)
        
        usuario_2 =  Usuario(  cedula = 8401133,
                            nombre = "Rafael",
                            apellido = "Hernandez",
                            edad = 59,
                            genero = "Masculino",
                            numero_hijos = 0)
        
        UsuariosController.insertar(usuario)
        UsuariosController.insertar(usuario_2)
        Usuario_buscado = UsuariosController.buscar_usuario(usuario_2.cedula)
        self.assertFalse(usuario.EsIgual(Usuario_buscado))

    def test_eliminar_normal_1(self):
        usuario =  Usuario(  cedula = 123456789,
                            nombre = "Elza",
                            apellido = "Pote",
                            edad = 71,
                            genero = "Femenino",
                            numero_hijos = 2)
        
        UsuariosController.insertar(usuario)
        UsuariosController.eliminar(usuario.cedula)
        self.assertIsNone(UsuariosController.buscar_usuario(usuario.cedula))


if __name__ == "__main__":
    unittest.main()