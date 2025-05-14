import unittest
import sys

sys.path.append("src")

from model.salarios import Salarios
from model.usuario import Usuario
from controller.salarios_controller import SalariosController
from controller.usuarios_controller import UsuariosController


class TestSalarios(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        SalariosController.borrar_tabla_salarios()
        UsuariosController.borrar_tabla()

        UsuariosController.crear_tabla()
        SalariosController.crear_tabla_salarios()

    def test_insertar_normal_1(self):
        usuario = Usuario(  cedula = 987654321,
                            nombre = "Simon",
                            apellido = "Correa",
                            edad = 85,
                            genero = "Masculino",
                            numero_hijos = 3)

        salarios = Salarios(cedula = usuario.cedula,
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
        SalariosController.insertar_datos_salarios(salarios)

        salarios_buscados = SalariosController.buscar_salarios(usuario.cedula)
        self.assertTrue(salarios.EsIgual(salarios_buscados))
    
    def test_eliminar(self):
        usuario = Usuario(  cedula = 135792468,
                            nombre = "Armando",
                            apellido = "Lalo quera",
                            edad = 72,
                            genero = "Masculino",
                            numero_hijos = 0)

        salarios = Salarios(cedula = usuario.cedula,
                            salario_1 = 3200000,
                            salario_2 = 3100000,
                            salario_3 = 3200000,
                            salario_4 = 5100000,
                            salario_5 = 3400000,
                            salario_6 = 3550000,
                            salario_7 = 3600000,
                            salario_8 = 3200000,
                            salario_9 = 3800000,
                            salario_10 = 3900000)
        
        UsuariosController.insertar(usuario)
        SalariosController.insertar_datos_salarios(salarios)

        SalariosController.eliminar(usuario.cedula)
        UsuariosController.eliminar(usuario.cedula)
        self.assertIsNone(SalariosController.buscar_salarios(usuario.cedula))


if __name__ == "__main__":
    unittest.main()