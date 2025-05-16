import sys
import time

sys.path.append("src")
sys.path.append(".")

from model import pylogic
from model.usuario import Usuario
from controller.usuarios_controller import UsuariosController

#Metodos
def asignar_genero(valor):
    match valor:
        case (1):
            return "Masculino"
        
        case (2):
            return "Femenino"
        
        case(3):
            raise ValueError("Selección inválida. Debe ser 1 (Masculino) o 2 (Femenino)")

def iniciar():
#Creacion de variables
    lista_salarios = []
    genero = ""
    edad = 0
    semanas = 0
    maximo_salarios = 11

    #Creacion de la tabla Usuarios
    UsuariosController.crear_tabla()

    # Comunicación con el usuario
    print("\n          Bienvenidos a la calculadora \n--------------------------------------------------\n\n")
    eleccion_tipo_usuario = int(input("Eres un Usuario: \n 1. Nuevo \n 2. Registrado \n\nSeleccion: "))

    if eleccion_tipo_usuario == 1:
        try:
            sleccionar_genero = int(input("\nPor favor selecciona tu género: \n\n 1. Masculino \n 2. Femenino \n\nSelección: "))
            genero = asignar_genero(sleccionar_genero)
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            cedula = input("Ingresa tu cedula: ")
            edad = int(input("Ingresa tu edad actual: "))
            semanas = int(input("Ingrese el total de semanas cotizadas: "))
            numero_hijos = int(input("¿Cuántos hijos tienes?: "))

            print("\n   Por favor ingresa tu salario de los últimos 10 años\n")

            lista_salarios = []
            for i in range(1, maximo_salarios):
                salario = int(input(f"Ingrese su salario {i}: "))
                lista_salarios.append(salario)
            
            usuario = Usuario(  cedula, nombre, apellido, edad, genero, numero_hijos, semanas,
                                lista_salarios[0], lista_salarios[1], lista_salarios[2],
                                lista_salarios[3], lista_salarios[4], lista_salarios[5],
                                lista_salarios[6], lista_salarios[7], lista_salarios[8], lista_salarios[9])
            UsuariosController.insertar(usuario)

        except Exception as error:
            print(f"\n❌ Error: {error} \n")

    elif eleccion_tipo_usuario == 2:
        cedula = int(input("Ingresa tu cedula registrada: "))
        usuario = UsuariosController.buscar_usuario(cedula)
        print(f"\n  Hola de nuevo {usuario.nombre}")
        time.sleep(1)

    else:
        print("Ingresaste una opcion invalida")
        time.sleep(1)
        iniciar()

    try:
        # Comunicación con la lógica
        salario_obtenido = UsuariosController.obtener_salarios(usuario.cedula)
        pension_total = pylogic.pension_total(salario_obtenido, usuario.genero, int(usuario.edad), int(usuario.semanas_cotizadas), int(usuario.numero_hijos))
        print(f"\n  {usuario.nombre} tu pension es: {pension_total}")

    except Exception as error:
        print(f"\n❌: {error} \n")
if __name__ == "__main__":
    iniciar()


#Corregir que hay que varios nombre de la lista de salarios