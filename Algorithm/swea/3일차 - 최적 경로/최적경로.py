import sys

sys.stdin = open('input.txt', 'r')


def perm_r_3(k):
    global result
    if k == N:
        if abs(arr[0][0] - arr[1][0]) + abs(arr[0][1] - arr[1][1]) not in result:
            result.append(abs(arr[0][0] - arr[1][0]) + abs(arr[0][1] - arr[1][1]))
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_3(k + 1)
            arr[k], arr[i] = arr[i], arr[k]





T = int(input())

for test_case in range(1, T+1):
    customer_count = int(input())
    location = list(map(int, input().split()))
    customer_location = [0] * (len(location) // 2)
    result = []
    a = 0
    for i in range(len(location)//2):
        customer_location[i] = [location[2*i], location[2*i+1]]
    work_location = customer_location.pop(0)
    home_location = customer_location.pop(0)
    my_max = 0
    arr = customer_location
    N = len(customer_location)
    perm_r_3(0)
    result.sort()
    for i in range(5):
        a += result[i]
    print(a)