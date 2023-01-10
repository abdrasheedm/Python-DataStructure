def changeLetter(string, key):
    list = []
    newKey = key % 26
    n = len(string)
    for i in range(n):
        letterPositon = ord(string[i]) + newKey
        if letterPositon <= 122:
            list.append(chr(letterPositon))
            print('jai')
        else:
            list.append(chr(96 + letterPositon % 122))

    return ''.join(list)

str = 'xyz'
print(2%26)
print(changeLetter(str, 2))
print(ord('z'))
#
#
# string = 'hai'
# string() = 'a'
# print(string[1])
for i in range(65, 123):
    print(chr(i), end=" ")