import sys

sys.stdin = open('input.txt', 'r')


# def perm(k, n, arr):
#     global my_min
#     if k == n:
#
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(k+1, n, arr)
#             arr[k], arr[i] = arr[i], arr[k]


def comb(n, r, arr, t):
    global my_min
    if r == 0:
        result_1 = t[:]
        result_2 = []
        first_result = 0
        second_result = 0
        for ii in range(size):
            if arr[ii] not in t:
                result_2.append(arr[ii])
        for re_1 in range(len(result_1)):
            for re_2 in range(len(result_1)):
                if not re_1 == re_2:
                    first_result += matrix[result_1[re_1]][result_1[re_2]] + matrix[result_1[re_2]][result_1[re_1]]
                    second_result += matrix[result_2[re_1]][result_2[re_2]] + matrix[result_2[re_2]][result_2[re_1]]
        real_result = abs(first_result-second_result)
        if my_min > real_result:
            my_min = real_result
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n - 1, r, arr, t)


T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    index_list = [jj for jj in range(size)]
    my_min = 10000000
    comb(size, size//2, index_list, [0]*(size//2))
    print('#{} {}'.format(test_case, my_min//2))


S2 = [x for x in A if x not in S1]