import sys

sys.stdin = open('input.txt', 'r')

def pi_r(a, t, k, n, r):
    if k == r:
        print(' '.join(map(str, t)))
    else:
        for i in range(n):
            t[k] = a[i]
            pi_r(a, t, k + 1, n, r)
num_1, num_2 = map(int, input().split())
num_list = [i+1 for i in range(num_1)]
N = len(num_list)
pi_r(num_list, [0]*num_2, 0, N, num_2)