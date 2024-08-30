# An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

def is_armstrong_number(number):
    number_digits = str(number)
    power = len(number_digits)
    result = 0
    for digit in number_digits:
        result += int(digit) ** power
    return number == result
