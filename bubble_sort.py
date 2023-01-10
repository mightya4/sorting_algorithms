def bubble_sort(array):
    index = len(array)
    while index >= 0:
        for j in range(index -1):
            #if current element is greater than next element swap elements
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        index -= 1
    return array

#test sort

sample_arr = [5, 8, 1, 6, 7, 2, 4, 3]
print("Test input")
print(*sample_arr, sep=" , ")
print(bubble_sort(sample_arr))