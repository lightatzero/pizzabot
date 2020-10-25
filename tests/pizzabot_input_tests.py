import pytest

from ..src.pizzabot_input import measure_input_string

def test_measure_input_string():
    assert measure_input_string("") == 0
