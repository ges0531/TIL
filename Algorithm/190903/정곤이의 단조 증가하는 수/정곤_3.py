import sys

sys.stdin = open('input.txt', 'r')


def increse(x):
    for li in range(len(x)-1):
        if x[li] > x[li+1]:
            return 0
    return 1


T = int(input())


for test_case in range(1, T+1):
    numbers = int(input())
    num_list = list(map(int, input().split()))
    a = 0
    for i in range(numbers):
        for j in range(i+1, numbers):
            if num_list[i]*num_list[j] >= 10 and increse(str(num_list[i]*num_list[j])) == 1 and a < num_list[i]*num_list[j]:
                a = num_list[i]*num_list[j]
    if a:
        print('#{} {}'.format(test_case, a))
    else:
        print('#{} -1'.format(test_case))