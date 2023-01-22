def palindromCheck(string):
    n = int(len(string) / 2)
    flag = 0
    for i in range(n):
        if string[i] != string[len(string) - 1 - i]:
            flag = 1
            break
    if flag == 0:
        print("string is palindrome")
    else:
        print("string is not palindrome")


name = 'hah'
palindromCheck(name)