def insertion_sort(array):
    for slot in range(1, len(array)):
        value = array[slot]
        test_slot = slot - 1
        #Compare Slot with previous slot and Swap if condition is met
        while test_slot > -1 and array[test_slot] > value:
            array[test_slot + 1] = array[test_slot]
            test_slot = test_slot - 1
        array[test_slot + 1] = value
    return array
    
#test sort

sample_arr = [5, 8, 1, 6, 7, 2, 4, 3]
print("Test input")
print(*sample_arr, sep=" , ")
print(insertion_sort(sample_arr))
