################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 3"""
def super_puestos(lista1, lista2):
    """Esta función se encarga de identificar los elementos que se superponen entre dos listas.
    Ademas indica la posicion de inicio de la superposición.
    """
    limite1 = len(lista1)
    limite2 = len(lista2)
    if limite1 > limite2:
        limite = limite1
        menor = limite2
        lista = lista2
    else:
        limite = limite2
        menor = limite1
        lista = lista1
    agregar = limite - menor
    contador = 0
    elemento = "ø"
    while contador != agregar:
        lista.append(elemento)
        contador = contador + 1
    posicion = 0
    elementos = 0
    superpuestos = []
    while posicion != limite:
        if lista1[posicion] == lista2[posicion]:
            elementos = elementos + 1
            superpuestos.append(posicion)
        posicion = posicion + 1
    extra = superpuestos[0]
    return elementos, extra
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    contador = 0
    lista1 = []
    lista2 = []
    limite = 0
    limite = int(input("¿Cuantos elementos desea ingresar en la primera lista? "))
    while contador != limite:
        contenido1 = input("Ingrese un elemento: ")
        contador = contador + 1
        lista1.append(contenido1)
    contador = 0
    limite = 0
    limite = int(input("¿Cuantos elementos desea ingresar en la segunda lista? "))
    while contador != limite:
        contenido2 = input("Ingrese un elemento: ")
        contador = contador + 1
        lista2.append(contenido2)
    respuesta = super_puestos(lista1, lista2)
    print(respuesta[0])
    print(f"La posición inicial del elemento superpuesto es la N° {respuesta[1]}")
if __name__ == "__main__":
    principal()
    