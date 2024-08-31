def rotate(text, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_upper = [letter.upper() for letter in alphabet]
    output_text = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + key
            output_text += alphabet[new_position]
        elif letter in alphabet_upper:
            position = alphabet_upper.index(letter)
            new_position = position + key
            output_text += alphabet_upper[new_position]
        else:
            output_text += letter
    return output_text
