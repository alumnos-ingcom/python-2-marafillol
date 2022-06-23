################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################ 
"""EJERCICIO 6"""
alfabeto = ["a", "b", "c", "d", "e", "f", 
"g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

contador = 0
posicion = 0

pregunta = ('¿Que desea realizar?')
print(pregunta)
print('< D > Decodificar')
print('< C > Codificar')
respuesta = input('')
if respuesta == 'C' or respuesta == 'c':
    texto = input("Ingrese algo: ")
    if texto.isnumeric():
        largo = len(texto)
        lista = []
        while texto != numeros[posicion]:
            posicion = posicion + 1
        if texto[posicion] == numeros[posicion]:
            lista.append(texto)
            
    elif texto.isalpha():
        print("Es una palabra")
    else:
        print("El dato ingresado no es valido, intentelo de nuevo.")
    