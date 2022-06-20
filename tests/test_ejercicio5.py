################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 5
"""
from practica.ejercicio5 import balance_corchetes
def test_balance_corchetes_true():
    """Esta función verifica si balance_corchetes
    funciona correctamente.
    """
    texto = '[]'
    resultado = balance_corchetes(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor boleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_balance_corchetes_false():
    """Esta función verifica si balance_corchetes
    funciona correctamente.
    """
    texto = ']['
    resultado = balance_corchetes(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor boleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_balance_corchetes_con_texto_true():
    """Esta función verifica si balance_corchetes
    funciona correctamente.
    """
    texto = '[hola][,][como][estas][?]'
    resultado = balance_corchetes(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor boleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_balance_corchetes_con_texto_false():
    """Esta función verifica si balance_corchetes
    funciona correctamente.
    """
    texto = ']hola[ ],[ ]como[ ]estas[ ]?['
    resultado = balance_corchetes(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor boleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_balance_corchetes_sin_corchetes():
    """Esta función verifica si balance_corchetes
    funciona correctamente.
    """
    texto = 'hola'
    resultado = balance_corchetes(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor boleano."
    assert resultado is True, "No se obtiene el resultado esperado."
    