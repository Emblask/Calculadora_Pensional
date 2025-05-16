import unittest
import sys

sys.path.append ("src")

from model.usuario import Usuario

from controller.usuarios_controller import UsuariosController

class TestUsuarios(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        UsuariosController.borrar_tabla()
        UsuariosController.crear_tabla()

    def test_insertar_normal_1(self):
        usuario = Usuario(  cedula = 1022145818,
                            nombre = "David",
                            apellido = "Hernandez",
                            edad = 71,
                            genero = "Masculino",
                            numero_hijos = 1,
                            semanas_cotizadas = 1300,
                            salario_1 = 4000000,
                            salario_2 = 3100000,
                            salario_3 = 3200000,
                            salario_4 = 3300000,
                            salario_5 = 3400000,
                            salario_6 = 3500000,
                            salario_7 = 3600000,
                            salario_8 = 3700000,
                            salario_9 = 3800000,
                            salario_10 = 3900000)
        
        UsuariosController.insertar(usuario)
        usuario_buscado = UsuariosController.buscar_usuario(usuario.cedula)
        self.assertTrue(usuario_buscado.EsIgual(usuario))
    
    def test_insertar_error_2(self):
        usuario =  Usuario( cedula = 43669647,
                            nombre = "Isabel",
                            apellido = "Trespalacios",
                            edad = 68,
                            genero = "Femenino",
                            numero_hijos = 2,
                            semanas_cotizadas = 1200,
                            salario_1 = 4500000,
                            salario_2 = 8100000,
                            salario_3 = 1200000,
                            salario_4 = 3000000,
                            salario_5 = 3000000,
                            salario_6 = 3000000,
                            salario_7 = 5000000,
                            salario_8 = 2700000,
                            salario_9 = 2000000,
                            salario_10 = 3900000)
        
        usuario_2 =  Usuario(  cedula = 8401133,
                            nombre = "Rafael",
                            apellido = "Hernandez",
                            edad = 59,
                            genero = "Masculino",
                            numero_hijos = 2,
                            semanas_cotizadas = 1250,
                            salario_1 = 4000000,
                            salario_2 = 7100000,
                            salario_3 = 7200000,
                            salario_4 = 1300000,
                            salario_5 = 8400000,
                            salario_6 = 5500000,
                            salario_7 = 5600000,
                            salario_8 = 5600000,
                            salario_9 = 1800000,
                            salario_10 = 5000000)
        
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
                            numero_hijos = 2,
                            semanas_cotizadas = 1340,
                            salario_1 = 4000000,
                            salario_2 = 3100000,
                            salario_3 = 3200000,
                            salario_4 = 3300000,
                            salario_5 = 3400000,
                            salario_6 = 3500000,
                            salario_7 = 3600000,
                            salario_8 = 3700000,
                            salario_9 = 3800000,
                            salario_10 = 3900000)
        
        UsuariosController.insertar(usuario)
        UsuariosController.eliminar(usuario.cedula)
        self.assertIsNone(UsuariosController.buscar_usuario(usuario.cedula))

    
    def test_eliminar_error_1(self):
        resutlado = UsuariosController.eliminar(147258369)
        self.assertEqual(resutlado, 0)


if __name__ == "__main__":
    unittest.main()