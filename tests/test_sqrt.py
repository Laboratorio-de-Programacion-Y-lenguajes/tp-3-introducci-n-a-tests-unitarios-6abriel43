"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
def test_sqrt_cero():
    assert sqrt(0) == 0.0  

def test_sqrt_no_cuadrado_perfecto():
    assert sqrt(5) == pytest.approx(2.2360679775)

def test_sqrt_negativo():
    with pytest.raises(ValueError):
        sqrt(-7)
