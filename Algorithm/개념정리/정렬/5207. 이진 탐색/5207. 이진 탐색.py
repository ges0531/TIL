import sys

sys.stdin = open('input.txt', 'r')


def binarySearch(n, S, key):
    low = 0
    high = n-1
    a = 0
    while low <= high:
        mid = (high+low)//2
        if S[mid] == key:
            return True
        elif S[mid] > key:
            high = mid - 1
            if a == 1:
                return False
            else:
                a = 1
        else:
            low = mid + 1
            if a == 2:
                return False
            else:
                a = 2
    return False


T = int(input())

for test_case in range(1, T+1):
    A_count, B_count = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    count = 0
    for i in range(len(B)):
        if binarySearch(len(A), A, B[i]):
            count += 1
    print('#{} {}'.format(test_case, count))

