import pytest

from pizzabot.engine import PizzabotEngine

from pizzabot.coordinates import PizzabotCoordinate, default_order


@pytest.fixture
def valid_small_engine():
    return PizzabotEngine()

def test_default_starting_postion(valid_small_engine):
    valid_small_engine.position == PizzabotCoordinate(0, 0, order=default_order)

def test_process_string(valid_small_engine):
    pe = PizzabotEngine()
    pe.process_string("5x5 (1, 3) (4, 4)")
    assert len(pe.journey) == 10
