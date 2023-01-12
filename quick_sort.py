def quick_sort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        #loop through each element and compare current element with pivot
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        #create subproblems until base case is reached
        less = quick_sort(less)
        more = quick_sort(more)
        #join lower, middle, upper array
        return less + pivotList + more

