################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 2
"""
from practica.ejercicio2 import estadistica
def test_estadistica_secuecia_positiva():
    """Esta función verifica si estadistica funciona correctamente.
    """
    secuencia = [5, 4, 3, 2, 1]
    resultado = estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0] == 5, "No se obtiene el resultado esperado."
    assert resultado[1] == 1, "No se obtiene el resultado esperado."
    assert resultado[2] == 3.0, "No se obtiene el resultado esperado."
def test_estadistica_secuecia_negativa():
    """Esta función verifica si estadistica funciona correctamente.
    """
    secuencia = [-1, -5, -3, -8]
    resultado = estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0] == -1, "No se obtiene el resultado esperado."
    assert resultado[1] == -8, "No se obtiene el resultado esperado."
    assert resultado[2] == -4.25, "No se obtiene el resultado esperado."
def test_estadistica_secuecia_positivos_y_negativos():
    """Esta función verifica si estadistica funciona correctamente.
    """
    secuencia = [-1, 0, 3, -4, 7]
    resultado = estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0] == 7, "No se obtiene el resultado esperado."
    assert resultado[1] == -4, "No se obtiene el resultado esperado."
    assert resultado[2] == 1.0, "No se obtiene el resultado esperado."
def test_estadistica_secuecia_de_ceros():
    """Esta función verifica si estadistica funciona correctamente.
    """
    secuencia = [0, 0, 0]
    resultado = estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0] == 0, "No se obtiene el resultado esperado."
    assert resultado[1] == 0, "No se obtiene el resultado esperado."
    assert resultado[2] == 0.0, "No se obtiene el resultado esperado."
    