def selectionSort(array):
    print(len(array))
    for i in range(len(array) - 1):
        print(i) 
        smallest = array[i]
        for j in range(i+1, len(array)):
            # print(j)
            if array[j] < smallest:
                smallest = array[j]
                array[j] = array[i]
                array[i] = smallest

    return array


array = [3, 2, 1, 54, 65, 234, 3]
print(selectionSort(array))
