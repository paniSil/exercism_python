def is_paired(input_string):
    brackets = ['(', ')', '[', ']', '{', '}']
    input_brackets = [b for b in input_string if b in brackets]
    check = []

    for bracket in input_brackets:
        check.append(bracket)
        if len(check) > 1:
            if bracket == ')' and '(' in check:
                check.pop()
                check.pop()
            elif bracket == ']' and '[' in check:
                check.pop()
                check.pop()
            elif bracket == '}' and '{' in check:
                check.pop()
                check.pop()
    return len(check) == 0
