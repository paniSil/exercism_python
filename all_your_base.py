def NumberFromBase(number, base):
    result = 0
    multiplier = len(number) - 1
    for digit in number:
        result += digit * base ** multiplier
        multiplier -= 1
    return result


def numberToBase(number, base):
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return digits[::-1]


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not digits:
        return [0]
    if any(digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base") 
    if any(digit < 0 for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    number = NumberFromBase(digits, input_base)
    result = numberToBase(number, output_base)
    return result
