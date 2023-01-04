def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def selectionSort(array):
    for i in range(len(array)):
        smallest = array[i]
        for j in range(i+1, len(array)):
            if smallest > array[j]:
                smallest = array[j]
                array[j] = array[i]
                array[i] = smallest

    return array



arr = [4, 1, 3, 87, 5, 32, 23]
print(bubbleSort(arr))
print(insertionSort(arr))
print(selectionSort(arr))

