import sys
sys.path.append("src")
from model import pylogic

#Metodos
def asignar_genero(valor):
    match valor:
        case (1):
            return "Masculino"
        
        case (2):
            return "Femenino"
        
        case(3):
            raise ValueError("Selección inválida. Debe ser 1 (Masculino) o 2 (Femenino)")

#Creacion de variables
lista_salarios = []
genero = ""
edad = 0
semanas = 0
maximo_salarios = 11

# Comunicación con el usuario
print("\n          Bienvenidos a la calculadora \n--------------------------------------------------\n\nPor favor ingresa tu salario de los últimos 10 años\n")

try:
    sleccionar_genero = int(input("Por favor selecciona tu género: \n\n 1. Masculino \n 2. Femenino \n\nSelección: "))
    genero = asignar_genero(sleccionar_genero)

    edad = int(input("Ingresa tu edad actual: "))
    semanas = int(input("Ingrese el total de semanas cotizadas: "))
    numero_hijos = int(input("¿Cuántos hijos tienes?: "))

    lista_salarios = []
    for i in range(1, maximo_salarios):
        salario = int(input(f"Ingrese su salario {i}: "))
        lista_salarios.append(salario)

    # Comunicación con la lógica
    print(pylogic.pension_total(lista_salarios, genero, edad, semanas, numero_hijos))

except Exception as e:
    print(f"\n❌ Error: {e}")


