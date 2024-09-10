def puissance(a, b):
    """
    Calcule a élevé à la puissance b.
    Vérifie que a et b sont des entiers.
    
    Lève une exception TypeError si ce n'est pas le cas.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Les arguments doivent être des entiers.")
    
    return a ** b

