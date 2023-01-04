

# size = len(arr)
# list1 = []
# for i in range(size):
#     for j in range(i+1, size):
#         if arr[i] + arr[j] == target:
#             list1 = [i, j]
#             break
#
# print(list1)
def two_sum():
    arr = [2, 7, 7, 11, 15]
    target = 9

    sett = {}
    for i in range(len(arr)):
        sett[arr[i]] = i
    print(sett)
    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment in sett and sett[compliment] != i:
            print(sett[compliment])
            return [i, sett[compliment]]


print(two_sum())







