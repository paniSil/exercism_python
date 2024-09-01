import math 


def score(x, y):
    c = math.sqrt(x**2 + y**2)

    if c <= 10:
        if c <= 5:
            if c <= 1:
                return 10
            return 5
        return 1
    else:
        return 0
