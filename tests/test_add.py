"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:

@pytest.mark.parametrize(
"a,b,expected",
[
(-2, -3, -5), #dos negativos
(5, -3, 2),   #positivo y negativo
(0, 0, 0),     #con cero
(1.5, 2.5, 4.0) #dos decimales
]
)
def test_add_parametrizado(a, b, expected):
    assert add(a, b) == pytest.approx(expected)
