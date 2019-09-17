def SelectionSort(A, s, e):
    if s == e:
        return
    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j
    A[s], A[mini] = A[mini], A[s]
    SelectionSort(A, s+1, e)
A = [3, 2, 5, 4, 1, 7, 9]
SelectionSort(A, 0, len(A))
print(A)
