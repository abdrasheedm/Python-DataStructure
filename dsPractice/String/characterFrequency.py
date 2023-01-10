def characterFrequncy(string):
    dict = {}
    for i in string:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict



string = 'hhhhaaaaaiiiii'
print(characterFrequncy(string))
