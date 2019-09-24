import sys

sys.stdin = open('input.txt', 'r')


def binarySearch(n, S, key):
    low = 0
    high = n-1
    while low <= high:
        mid = (high+low)//2
        if S[mid] == key:
            return True
        elif S[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return False

T = int(input())

for test_case in range(1, T+1):
    immigration, people = map(int, input().split())
    immigration_time = [int(input()) for _ in range(immigration)]
    my_min = 10000000000000000
    for i in range(immigration):
        if my_min > immigration_time[i]:
            my_min = immigration_time[i]
    print(binarySearch(immigration, immigration_time, my_min))