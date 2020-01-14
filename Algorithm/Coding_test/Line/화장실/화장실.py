import sys

sys.stdin = open('input.txt', 'r')

T = 3

for test_case in range(1, T+1):
    application_count = int(input())
    restroom_time = [list(map(int, input().split())) for _ in range(application_count)]
    restroom_time.sort(key=lambda x: x[1])
    count = 0
    a = restroom_time[0][1]
    for i in range(len(restroom_time)):
        if restroom_time[i][0] >= a:
            a = restroom_time[i][1]
        else:
            count += 1
    print(count)
