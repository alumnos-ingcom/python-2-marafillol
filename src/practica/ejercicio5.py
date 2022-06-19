################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 5"""
def balance_corchetes(texto):
    """Esta funcion determina si los corchetes de una cadena
    ingresada por el usuario tienen su par correspondiente.
    """
    texto = list(texto)
    limite = len(texto)
    posicion = 0
    contador = 0
    corchetes = []
    while contador != limite:
        if texto[posicion] == "[":
            corchetes.append(texto[posicion])
        elif texto[posicion] == "]":
            corchetes.append(texto[posicion])
        posicion = posicion + 1
        contador = contador + 1
    limite = len(corchetes)
    contador = limite
    if limite > 1:
        while limite != 0:
            if corchetes[0]== "[" and corchetes[-1]=="]":
                corchetes.remove("[")
                corchetes.remove("]")
                contador = contador -2
            limite = limite - 2
        respuesta = contador ==0
    elif limite == 0:
        respuesta = True
    else:
        respuesta = False
    return respuesta
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto = input("Ingrese una cadena: ")
    resultado = balance_corchetes(texto)
    print(resultado)
if __name__ == "__main__":
    principal()
