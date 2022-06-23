################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 4"""
def fibonacci(termino):
    """ Esta función obtiene el termino ingresado por el usuario
    de la sucesión de Fibonacci.
    """
    numeros = [1, 1]
    posicion = 0
    contador = 0
    while contador != (termino-2):
        suma = numeros[posicion] + numeros[(posicion+1)]
        numeros.append(suma)
        posicion = posicion + 1
        contador = contador + 1
        resultado = suma
    return resultado
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    termino = 0
    while termino <= 2:
        termino = int(input(" Ingrese el n-ésimo término de la sucesión Fibonacci: "))
        if termino > 2:
            respuesta = fibonacci(termino)
            print(f"\n El término N° {termino} de la sucesión Fibonacci es el número {respuesta}.")
        else:
            respuesta = "\n El término debe ser mayor a 2, intentelo de nuevo.\n"
            print(respuesta)
if __name__ == "__main__":
    principal()
    