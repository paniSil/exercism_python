def label(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    value = ''
    if colors[0] != 'black':
        value += str(color_list.index(colors[0]))
    value += str(color_list.index(colors[1]))

    zero_q = color_list.index(colors[2])
    if zero_q > 0:
        for n in range(zero_q):
            value += '0'

    if value.endswith('000000000'):
        value = value.replace('000000000', '')
        return value + ' gigaohms'
    elif value.endswith('000000'):
        value = value.replace('000000', '')
        return value + ' megaohms'
    elif value.endswith('000'):
        value = value.replace('000', '')
        return value + ' kiloohms'
    else:
        return value + ' ohms'
