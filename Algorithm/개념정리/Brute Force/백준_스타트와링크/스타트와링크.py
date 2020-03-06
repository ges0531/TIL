import sys

sys.stdin = open('input.txt', 'r')


def calc_team(array):
    result = 0
    for i in array:
        for j in array:
            if not i == j:
                result += matrix[i][j]
    return result


def comb(n, r, arr, t):
    global my_min
    if r == 0:
        another_t = [x for x in arr if x not in t]
        real_result = abs(calc_team(t) - calc_team(another_t))
        if my_min > real_result:
            my_min = real_result
        return
    elif r > n:
        return
    t[r-1] = arr[n-1]
    comb(n-1, r-1, arr, t)
    comb(n-1, r, arr, t)




people_count = int(input())
matrix = [list(map(int, input().split())) for _ in range(people_count)]
people_num = [i for i in range(people_count)]
my_min = 1000000
comb(people_count, people_count//2, people_num, [0]*(people_count//2))
print(my_min)
