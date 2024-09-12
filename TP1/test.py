import pytest
import fonctions as f

def test_puissance_basiques():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_puissance_base_negative():
    assert f.puissance(-2, 3) == -8  # Base négative et exposant impair
    assert f.puissance(-2, 2) == 4   # Base négative et exposant pair
    assert f.puissance(-2, 0) == 1   # Base négative et exposant nul

def test_puissance_exposant_negatif():
    with pytest.raises(ValueError):
        f.puissance(2, -2)  # La fonction devrait lancer une exception pour les exposants négatifs

def test_puissance_base_zero():
    assert f.puissance(0, 5) == 0     # Base nulle et exposant positif
    assert f.puissance(0, 0) == 1     # Base nulle et exposant nul

def test_puissance_exposant_zero():
    assert f.puissance(5, 0) == 1     # Base positive et exposant nul

def test_puissance_valeurs_larges():
    assert f.puissance(10, 6) == 1000000  # Valeurs élevées
    assert f.puissance(2, 20) == 1048576  # Valeurs élevées

def test_puissance_base_non_entier():
    with pytest.raises(TypeError):
        f.puissance(2.5, 3)  # La fonction devrait lancer une exception pour les bases non entières

def test_puissance_exposant_non_entier():
    with pytest.raises(TypeError):
        f.puissance(2, 3.5)  # La fonction devrait lancer une exception pour les exposants non entiers

def test_puissance_base_zero_exposant_negatif():
    with pytest.raises(ZeroDivisionError):
        f.puissance(0, -1)  # La fonction devrait lancer une exception pour 0 élevé à une puissance négative

