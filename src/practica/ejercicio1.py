################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 1"""
def pares_e_impares(numero):
    """Esta función determina si el número ingresado
    es par o impar"""
    numero = abs(numero)
    limite = numero
    contador = 0
    while contador != limite:
        while numero > 0:
            numero = numero - 2
        contador = contador + 1
    resultado = numero == 0
    return resultado
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número: "))
    resultado = pares_e_impares(numero)
    print(resultado)
if __name__ == "__main__":
    principal()
