def is_isogram(string):
    string = string.lower()
    result = ''
    exclusions = ' -'
    for char in string:
        if char not in result:
            result += char
        else:
            if char in exclusions:
                continue
            else:
                return False
    return True
