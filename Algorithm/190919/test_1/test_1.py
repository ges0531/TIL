def quickSort(A, l, r):
    if l < r:
        s = partition_2(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1
def partition_2(A, l, r):
    p = A[l]
    i = l
    j = r
    while i < j:
        while A[i] <= p and i < r:
            i += 1
        while A[j] >= p and j > l:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j



A = [11, 45, 23, 81, 28, 34]
quickSort(A, 0, len(A)-1)
print(A)
B = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
quickSort(B, 0, len(B)-1)
print(B)
C = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
quickSort(C, 0, len(C)-1)
print(C)