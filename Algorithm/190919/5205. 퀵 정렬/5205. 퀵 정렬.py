import sys

sys.stdin = open('input.txt', 'r')


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


T = int(input())

for test_case in range(1, T+1):
    num_count = int(input())
    num_list = list(map(int, input().split()))
    n = len(num_list)
    quickSort(num_list, 0, n-1)
    print('#{} {}'.format(test_case, num_list[n//2]))