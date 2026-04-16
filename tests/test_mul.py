"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize( "a,b,expected",     
[
(8, 0, 0),        # Multiplicar por cero
(-2, -7, 14),     # Multiplicar dos negativos
(8, -3, -24),     # Multiplicar un positivo y un negativo
(2, 1, 2),        # Multiplicar por 1
(5.6, 2.5, 14.0)  # Multiplicar dos decimales
])

def test_mul_parametrizado(a, b, expected):
    assert mul(a, b) == pytest.approx(expected)