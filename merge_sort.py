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
        result.extend(right[right_idx])
    return result