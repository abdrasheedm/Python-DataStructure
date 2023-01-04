def binarySearch(array, beg, end, value):
    print(beg)
    if end >= beg:
        mid = int((beg + end) / 2)
        print(mid)
        print('-----')

        if array[mid] == value:
            return mid + 1
        elif array[mid] < value:
            return binarySearch(array, mid + 1, end, value)
        else:
            return binarySearch(array, beg, mid - 1, value)

    return - 1


array1 = [10, 12, 24, 29, 34, 40, 51, 56, 69]
beg = 0
end = len(array1) - 1
print(end)
value = 51
print(binarySearch(array1, beg, end, value))


