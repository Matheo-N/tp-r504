def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Les arguments doivent être des entiers.")
    
    return a ** b

