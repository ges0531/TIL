import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    immigration, people = map(int, input().split())
    immigration_time = [int(input()) for _ in range(immigration)]
    immigration_time_2 = [immigration_time[j] for j in range(len(immigration_time))]
    index = 0
    cnt = 0
    while cnt < people-1:
        my_min = 100000000000000
        for i in range(len(immigration_time_2)):
            if my_min > immigration_time_2[i]:
                my_min = immigration_time_2[i]
                index = i
        immigration_time_2[index] += immigration_time[index]
        cnt += 1
    print('#{} {}'.format(test_case, immigration_time_2[index]))