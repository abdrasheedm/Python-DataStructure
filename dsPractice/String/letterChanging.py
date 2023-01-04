def changeLetter(string, key):
    newKey = key % 26
    for i in string:
        print(ord(i), newKey)
        letterPositon = ord(i) + newKey
        print(letterPositon)
        if letterPositon <= 122:
            string = string.replace(i, chr(letterPositon))
        else:
            string = string.replace(i, chr(97 + letterPositon % 122))

    return string

str = 'abc'
print(changeLetter(str, 2))
print(ord('z'))

