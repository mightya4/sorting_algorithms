#Merge function serves to join left and right arrays into a sorted array
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    #append to result any elements left in list after merge
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    #If array has at least one element return the array of that element
    if len(m) <= 1:
        return m

    #divide the array has evenly as possible and save to left and right array
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    #divide elements until down to base case
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

    #test sort

sample_arr = [5, 8, 1, 6, 7, 2, 4, 3]
print("Test input")
print(*sample_arr, sep=" , ")
print(merge_sort(sample_arr))
