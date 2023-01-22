# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def changeLetter(string):
    char = string[0]
    newString = string.replace(char, '$')
    newString = char + newString[1:]

    return newString

name = 'rasherasdfra'
print(changeLetter(name))