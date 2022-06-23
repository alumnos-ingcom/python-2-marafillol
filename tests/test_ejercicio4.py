################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 4
"""
from practica.ejercicio4 import fibonacci
#Teniendo en cuenta que los primeros 2 terminos de
#la sucesion de Fibonacci es 1...
def test_fibonacci_termino_mayor_a_dos():
    """Esta función verifica si fibonacci
    funciona correctamente.
    """
    termino = 13
    resultado = fibonacci(termino)
    assert isinstance(resultado, int), "El resultado debe ser un int"
    assert resultado == 233, "No se obtiene el resultado esperado."
def test_fibonacci_termino_es_dos():
    """Esta función verifica si fibonacci
    funciona correctamente.
    """
    termino = 2
    resultado = fibonacci(termino)
    assert isinstance(resultado, int), "El resultado debe ser un int"
    assert resultado == 0, "No se obtiene el resultado esperado."
def test_fibonacci_termino_es_cero():
    """Esta función verifica si fibonacci
    funciona correctamente.
    """
    termino = 0
    resultado = fibonacci(termino)
    assert isinstance(resultado, int), "El resultado debe ser un int"
    assert resultado == 0, "No se obtiene el resultado esperado."
def test_fibonacci_termino_es_uno():
    """Esta función verifica si fibonacci
    funciona correctamente.
    """
    termino = 1
    resultado = fibonacci(termino)
    assert isinstance(resultado, int), "El resultado debe ser un int"
    assert resultado == 0, "No se obtiene el resultado esperado."
def test_fibonacci_termino_es_positivo():
    """Esta función verifica si fibonacci
    funciona correctamente.
    """
    termino = 6
    resultado = fibonacci(termino)
    assert isinstance(resultado, int), "El resultado debe ser un int"
    assert resultado == 8, "No se obtiene el resultado esperado."
def test_fibonacci_termino_es_negativo():
    """Esta función verifica si fibonacci
    funciona correctamente.
    """
    termino = -3
    resultado = fibonacci(termino)
    assert isinstance(resultado, int), "El resultado debe ser un int"
    assert resultado == 0, "No se obtiene el resultado esperado."
    