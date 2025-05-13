import unittest
import sys

sys.path.append ("src")

from model.usuario import Usuario

from controller.usuarios_controller import UsuariosController

class TestTarjeta(unittest.TestCase):
    def setUpClass():
        UsuariosController.borrar_tabla()
        UsuariosController.crear_tabla()

#Continuar con las pruebas