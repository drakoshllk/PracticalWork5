import math

def is_in_circle(x, y, radius):
    hypotenuse = math.sqrt(pow(x, 2) + pow(y, 2))
    if hypotenuse <= radius:
        return True
    else:
        return False