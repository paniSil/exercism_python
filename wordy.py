def answer(question):
    question = question[8:-1]

    if question.replace(' ', '').isalpha():
        raise ValueError('unknown operation')
    if 'cubed' in question:
        raise ValueError('unknown operation')

    if question.isdigit(): 
        return int(question)

    if 'plus' in question or 'minus' in question or 'multiplied' in question or 'divided' in question:
        question = question.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/").split(' ')

        try:
            result = int(question[0])
            for symbol in range(1, len(question), 2):
                operator = question[symbol]
                num = int(question[symbol+1])
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    result /= num
            return result
        except:
            raise ValueError("syntax error")
    else:
        raise ValueError("syntax error")