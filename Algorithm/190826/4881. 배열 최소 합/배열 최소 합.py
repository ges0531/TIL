import sys


sys.stdin = open('input.txt', 'r')

def perm_r(k):
    global my_min
    if k == R:
        row = 0
        my_sum = 0
        for z in t:
            my_sum += matrix[z - 1][row]
            row += 1
            if my_sum > my_min:
                break
        if my_min > my_sum:
            my_min = my_sum
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = i + 1
            visited[i] = 1
            perm_r(k + 1)
            visited[i] = 0


T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    N = R = size
    t = [0] * N
    visited = [0] * N
    my_min = 0
    matrix = [list(map(int, input().split())) for _ in range(size)]
    for j in range(len(matrix)):
        my_min += matrix[j][j]
    perm_r(0)
    print('#{} {}'.format(test_case, my_min))
