import sys

sys.stdin = open('input.txt', 'r')

def H_r(a, t, k, n, r, s):
    if k == r:
        print(' '.join(map(str, t)))
    else:
        for i in range(s, n):
            t[k] = a[i]
            H_r(a, t, k + 1, n, r, i)


num_1, num_2 = map(int, input().split())
num_list = [i+1 for i in range(num_1)]

H_r(num_list, [0]*num_2, 0, num_1, num_2, 0)