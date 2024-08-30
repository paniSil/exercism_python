# not very elegant

def translate_word(text):
    vowels = ['a', 'e', 'i', 'o', 'u']

    # starts with vowel or 'xr' or 'yt'
    if text[0] in vowels or text[:2] == 'xr' or text[:2] == 'yt':
        return text + 'ay'

    # first letter not a vowel
    elif text[0] not in vowels:

        #first two letters not vowels or starts with 'qu'
        if text[1] not in vowels or text[:2] == 'qu':    

            # 'qu' after fisrt letter
            if text[1:3] == 'qu':      
                return text[3:] + text[:3] + 'ay'

            # 'y' is the second letter
            elif text[1] == 'y':       
                return text[1:] + text[:1] + 'ay'

            # first three letters not vowels
            elif text[2] not in vowels:

                # y is a vowel in that case
                if text[2] == 'y':
                    return text[2:] + text[:2] + 'ay'

                return text[3:] + text[:3] + 'ay'

            return text[2:] + text[:2] + 'ay'

        else:
            return text[1:] + text[:1] + 'ay'


def translate(text):
    # for one word
    if text == text.replace(' ', ''):
        return translate_word(text)

    # for sentences
    else:
        return ' '.join([translate_word(word) for word in text.split()])
