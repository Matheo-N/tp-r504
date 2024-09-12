import pytest
import fonctions as f

def test_puissance_basic():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_puissance_negative_base():
    assert f.puissance(-2, 3) == -8  # Base négative et exposant impair
    assert f.puissance(-2, 2) == 4   # Base négative et exposant pair
    assert f.puissance(-2, 0) == 1   # Base négative et exposant nul

def test_puissance_negative_exponent():
    assert f.puissance(2, -2) == 0.25  # Base positive et exposant négatif

def test_puissance_zero_base():
    assert f.puissance(0, 5) == 0     # Base nulle et exposant positif
    assert f.puissance(0, 0) == 1     # Base nulle et exposant nul

def test_puissance_zero_exponent():
    assert f.puissance(5, 0) == 1     # Base positive et exposant nul

def test_puissance_large_values():
    assert f.puissance(10, 6) == 1000000  # Valeurs élevées
    assert f.puissance(2, 20) == 1048576  # Valeurs élevées

def test_puissance_edge_cases():
    # Cas limites supplémentaires pour tester la robustesse
    assert f.puissance(1, 1000) == 1    # Base unitaire
    assert f.puissance(-1, 1000) == 1   # Base unitaire négative
    assert f.puissance(2, 0.5) == 1.4142135623730951  # Exposant fractionnaire (racine carrée de 2)


