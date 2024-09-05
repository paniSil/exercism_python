alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode(plain_text):
    encoded_text = ''
    text = plain_text.replace(' ', '')
    for char in text:
        if char.isalpha():
            char_index = alphabet.find(char.lower())
            encoded_text += alphabet[- char_index - 1]
        elif char.isdigit():
            encoded_text += char
    encoded_text_parted = [encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)]
    encoded_text_parted = ' '.join(encoded_text_parted)
    return encoded_text_parted


def decode(ciphered_text):
    decoded_text = ''
    ciphered_text = ciphered_text.replace(' ', '')
    for char in ciphered_text:
        if char.isalpha():
            char_index = alphabet.find(char)
            decoded_text += alphabet[- char_index - 1]
        elif char.isdigit():
            decoded_text += char
    return decoded_text
