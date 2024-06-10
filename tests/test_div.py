# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación div
    def test_div(self):
        assert div(4,2) == 2
        assert div(6,-3) == 2
        assert div(12,6) == 2
        assert div(24,12) == 2
