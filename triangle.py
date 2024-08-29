# checking if the given triangle s equilaterial, isosceles or scalene


def is_triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return False
    else:
        return a + b >= c and b + c >= a and a + c >= b


def equilateral(sides):
    a, b, c = sides
    if is_triangle(a, b, c):
        return a == b == c
    else:
        return False


def isosceles(sides):
    a, b, c = sides
    if is_triangle(a, b, c):
        return a == b or b == c or c == a
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if is_triangle(a, b, c):
        return a != b != c != a
    else:
        return False
