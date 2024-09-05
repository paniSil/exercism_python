def classify(number):
    divisors_sum = 0
    if number > 0:
        for n in range(1, number):
            if number % n == 0:
                divisors_sum += n

        if divisors_sum == number:
            return 'perfect'
        elif divisors_sum > number:
            return 'abundant'
        else:
            return 'deficient'
    else:
        raise ValueError('Classification is only possible for positive integers.')
