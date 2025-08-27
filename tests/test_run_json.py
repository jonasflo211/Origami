import os
import pytest
from examples.run_prueba import run_circuit_from_json

def test_prueba_json():
    result = run_circuit_from_json("prueba.json")

    # Normalizar claves y valores
    result_normalized = {
        "sum": int(result["s"]),
        "carry": int(result["c"])
    }

    expected = {"sum": 1, "carry": 0}

    assert result_normalized == expected, f"Resultado inesperado: {result_normalized}"
