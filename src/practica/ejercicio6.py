################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 6"""
alfabeto = ["a", "b", "c", "d", "e", "f", 
"g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
codificar = []
decodificar = []
contador = 0

posicion = 0

pregunta = ('¿Que desea realizar? ')
print(pregunta)
print('< D > Decodificar')
print('< C > Codificar')
respuesta = input('')
if respuesta == 'C' or respuesta == 'c':
    frase = frase = ('hola mundo')
    rotaciones = 13
    limite = len(frase)
    while contador != limite:
        codificar.append(limite)
    print(codificar)