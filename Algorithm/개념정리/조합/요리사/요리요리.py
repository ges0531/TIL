import sys

sys.stdin = open('input.txt', 'r')


def comb(n, r, arr, t):
    global my_min
    if r == 0:
        result_2 = [x for x in arr if x not in t]
        first_result = 0
        second_result = 0
        for re_1 in range(len(t)):
            for re_2 in range(len(t)):
                first_result += matrix[t[re_1]][t[re_2]] + matrix[t[re_2]][t[re_1]]
                second_result += matrix[result_2[re_1]][result_2[re_2]] + matrix[result_2[re_2]][result_2[re_1]]
        my_min = min(my_min, abs(first_result-second_result))
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