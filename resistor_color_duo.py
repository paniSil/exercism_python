def value(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    value = ''
    value += str(color_list.index(colors[0]))
    value += str(color_list.index(colors[1]))
    return int(value)
