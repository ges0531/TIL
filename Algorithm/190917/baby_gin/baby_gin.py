import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n):
    global result
    if k == n:
        if (a[0] + 1) == a[1] and (a[1] + 1) == a[2]:
            if a[3] == a[4] and a[4] == a[5]:
                result = 1
            elif (a[3] + 1) == a[4] and (a[4] + 1) == a[5]:
                result = 1
        elif a[0] == a[1] and a[1] == a[2]:
            if a[3] == a[4] and a[4] == a[5]:
                result = 1
            elif (a[3] + 1) == a[4] and (a[4] + 1) == a[5]:
                result = 1
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(k+1, n)
            a[i], a[k] = a[k], a[i]

T = int(input())

for test_case in range(1, T+1):
    a = list(map(int, input()))
    result = 0
    perm(0, len(a))
    if result == 1:
        print('baby_gin')
    else:
        print('no no')
