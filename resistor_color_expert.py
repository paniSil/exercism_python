def resistor_label(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    tolerance_dict = {
        'grey': '0.05%',
        'violet': '0.1%',
        'blue': '0.25%',
        'green': '0.5%',
        'brown': '1%',
        'red': '2%',
        'gold': '5%',
        'silver': '10%'
    }

    value = ''
    if colors[0] != 'black':
        value += str(color_list.index(colors[0]))
    elif colors[0] == 'black' and len(colors) < 2:
        return '0 ohms'

    value += str(color_list.index(colors[1]))

    if len(colors) == 5:
        value += str(color_list.index(colors[2]))
        zero_q = color_list.index(colors[3])
        tolerance = tolerance_dict[colors[4]]
    else:
        zero_q = color_list.index(colors[2])
        tolerance = tolerance_dict[colors[3]]

    if zero_q > 0:
        for n in range(zero_q):
            value += '0'

    if len(value) > 9:
        value = int(value)/1000000000
        if value.is_integer():
            value = int(value)
        return f'{value} gigaohms ±{tolerance}'
    elif len(value) > 6:
        value = int(value)/1000000
        if value.is_integer():
            value = int(value)
        return f'{value} megaohms ±{tolerance}'
    elif len(value) > 3:
        value = int(value)/1000
        if value.is_integer():
            value = int(value)
        return f'{value} kiloohms ±{tolerance}'
    else:
        return f'{value} ohms ±{tolerance}'
