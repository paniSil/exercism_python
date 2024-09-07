def rows(letter):
    result = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rows = alphabet.index(letter)
    diamond = []
    letter_index = 0
    letter_place = rows
    for r in range(rows + 1):
        diamond.append([' ' for x in range(rows + 1)])
        diamond[r][letter_place] = alphabet[letter_index]
        letter_place -= 1
        letter_index += 1

    for row in diamond:
        row_reversed = row.copy()
        row_reversed.reverse()
        row_reversed.pop(0)
        row += row_reversed

    diamond_bottom = diamond.copy()
    diamond_bottom.reverse()
    diamond_bottom.pop(0)
    diamond += diamond_bottom

    for row in diamond:
        result.append(''.join(row))
    return result
