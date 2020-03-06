import sys


sys.stdin = open('input.txt', 'r')

T = int(input())
A = [0]*12
for A_set in range(0, 12):
    A[A_set] = A_set+1
for test_case in range(1, T+1):
    count = 0
    sub_set_count, sum_set = map(int, input().split())
    for i in range(1, 1 << len(A)):
        sub_set = []
        for j in range(len(A)):
            if i & (1 << j):
                sub_set.append(A[j])
        if len(sub_set) == sub_set_count and sum(sub_set) == sum_set:
                count += 1
    print('#{} {}'.format(test_case, count))