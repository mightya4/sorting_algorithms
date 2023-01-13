#Takes inputs Array A, digit to sort by, and radix as base of number system
def counting_sort(A, digit, radix):
    #Array B will be the fully sorted list to return
    B = [0] * len(A)
    C = [0] * int(radix)
    
    for i in range(0, len(A)):
        digit_of_Ai = (A[i]/radix**digit)%radix
        C[digit_of_Ai] = C[digit_of_Ai] + 1
        #each element i in C contains the value of number of elements in A equal to i

    for j in range(1, radix):
        C[j] = C[j] + C[j-1]

    for m in range(len(A)-1, -1, -1):
        digit_of_Ai = (A[m]/radix**digit)%radix
        C[digit_of_Ai] = C[digit_of_Ai] - 1
        B[C[digit_of_Ai]] = A[m]

    return B