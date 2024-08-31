def is_valid(isbn):
    digits_for_check = '0123456789'
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    isbn = list(isbn)
    
    for char in isbn:
        if char not in digits_for_check:
            if isbn.index(char) == len(isbn) - 1:
                if char == 'X':
                    isbn[-1] = 10
                else:
                    return False
            else:
                return False
            
    isbn = [int(digit) for digit in isbn]
    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = isbn
    result = (d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2 + d10 * 1) % 11
    return result == 0
