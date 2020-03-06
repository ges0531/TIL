import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    str_1 = input()
    str_2 = input()
    M = len(str_1)
    N = len(str_2)
    i = 0
    j = 0
    while j < M and i < N:
        if str_2[i] != str_1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))

