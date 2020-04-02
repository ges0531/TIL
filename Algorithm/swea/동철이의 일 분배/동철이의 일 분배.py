import sys

sys.stdin = open('input.txt', 'r')


# def perm(k, n, a):
#     if k == n:
#         print(a)
#     else:
#         for i in range(k, n):
#             a[i], a[k] = a[k], a[i]
#             perm(k+1, n, a)
#             a[i], a[k] = a[k], a[i]

T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    work_efficient = [list(map(int, input().split())) for _ in range(N)]
    
    # for j in range(len(work_efficient)):
    #     perm(0, len(work_efficient[j]), work_efficient[j])
