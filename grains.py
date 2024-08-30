# Calculate the number of grains of wheat on a chessboard given that the
# number on each square doubles.


def square(number):
    grains = 1
    if number == 1:
        return grains
    elif 1 < number < 65:
        for n in range(1, number):
            grains *= 2
    else:
        raise ValueError('square must be between 1 and 64')
    return grains


def total():
    sum = 0
    for n in range(1, 65):
        sum += square(n)
    return sum
