import sys


sys.stdin = open('input.txt', 'r')

T = int(input())


def backtrack(a, k, input):
    global MAXCABDIDATES
    c = [0] * MAXCABDIDATES
    if k == input:
        z = 0
        my_sum = 0
        for i in range(1, k+1):
            my_sum += matrix[a[i]][z]
            z += 1
        my_box.append(my_sum)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
    print(my_box)

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


for test_case in range(1, T+1):
    print(test_case, '-')
    MAXCABDIDATES = 100
    NMAX = 100
    a = [0] * NMAX
    size = int(input())
    my_box = []
    matrix = [list(map(int, input().split())) for _ in range(size)]
    matrix.reverse()
    matrix.append([0]*size)
    matrix.reverse()
    stack = []
    visited = [[0] * size for _ in range(size)]
    backtrack(a, 0, size)

