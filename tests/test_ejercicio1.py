################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 1
"""
from practica.ejercicio1 import pares_e_impares
def test_pares_e_impares_si_es_par():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = 2
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_impar():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = 3
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_uno():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = 1
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_cero():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = 0
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_positivo_par():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = 12
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_positivo_impar():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = 7
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_negativo_par():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = -2
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_pares_e_impares_si_es_negativo_impar():
    """Esta función verifica si pares_e_impares funciona correctamente.
    """
    numero = -1
    resultado = pares_e_impares(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
    