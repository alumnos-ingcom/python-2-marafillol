################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 3
"""
from practica.ejercicio3 import super_puestos
#El primer número indica cuantos elementos se superponen.
#El segundo número indica cual fue la posicion del primer
#número que se superpuso.
#La posicion del elemento que se superpone se cuenta desde 0. 
def test_super_puestos_todos_los_elementos():
    """Esta función verifica si super_puestos
    funciona correctamente.
    """
    lista1 = ['h', 'o', 'l', 'a']
    lista2 = ['h', 'o', 'l', 'a']
    resultado = super_puestos(lista1, lista2)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (4, 0), "No se obtiene el resultado esperado."
def test_super_puestos_no_se_superpone_un_elemento():
    """Esta función verifica si super_puestos
    funciona correctamente.
    """
    lista1 = ['h', 'o', 'l', 'o']
    lista2 = ['h', 'o', 'l', 'a']
    resultado = super_puestos(lista1, lista2)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (3, 0), "No se obtiene el resultado esperado."
def test_super_puestos_no_se_superpone_ningun_elemento():
    """Esta función verifica si super_puestos
    funciona correctamente.
    """
    lista1 = ['m', 'a', 'r', 'a']
    lista2 = ['a', 'm', 'o', 'r']
    resultado = super_puestos(lista1, lista2)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0, 0), "No se obtiene el resultado esperado."
def test_super_puestos_no_hay_ningun_elemento():
    """Esta función verifica si super_puestos
    funciona correctamente.
    """
    lista1 = []
    lista2 = []
    resultado = super_puestos(lista1, lista2)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0, 0), "No se obtiene el resultado esperado."
    