"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize(
"a,b,expected",     
[
(4, 5, -1),         # Restar un número mayor al primero
(8, 0, 8),          # Restar cero
(-3, -3, 6),        # Restar dos números negativos
(5.2, 2.9, 2.3)     # Restar dos números decimales
]
)
def test_sub_parametrizado(a, b, expected):
    assert sub(a, b) == pytest.approx(expected)