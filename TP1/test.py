import pytest
import fonctions as f

def test_1():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_2():
    assert f.puissance(-2, 3) == -8  # Base négative et un exposant impair
    assert f.puissance(-2, 2) == 4   # Base négative et un exposant pair
    assert f.puissance(-2, 0) == 1   # Base négative et un exposant nul
    assert f.puissance(2, -2) == 0.25  # Base positive et un exposant négatif

