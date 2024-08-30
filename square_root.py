# Given a natural radicand, return its square root.


def square_root(number):
    root = 1
    while not root ** 2 == number:  # while loop is not ideal for large numbers
        root += 1
    return root
