################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 2"""
def estadistica(secuencia):
    """Esta función se encarga de calcular el maximo, minimo y
    el promedio de una secuencia de números elegida por el usuario.
    (maximo, minimo, promedio)
    """
    limite = len(secuencia)
    contador = 0
    posicion = 0
    minimo = secuencia[posicion]
    maximo = secuencia[posicion]
    promedio = 0
    while contador != limite:
        if secuencia[posicion] < minimo:
            minimo = secuencia[posicion]
        if secuencia[posicion] > maximo:
            maximo = secuencia[posicion]
        promedio = promedio + secuencia[posicion]
        posicion = posicion + 1
        contador = contador + 1
    promedio = promedio / limite
    resultado = (maximo, minimo, promedio)
    return resultado
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    limite = int(input("¿Cuantos números desea ingresar? "))
    contador = 0
    secuencia = []
    while contador != limite:
        numero = int(input("Ingrese un número: "))
        contador = contador + 1
        secuencia.append(numero)
    respuesta = estadistica(secuencia)
    print(respuesta)
if __name__ == "__main__":
    principal()
