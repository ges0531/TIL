import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    application_count = int(input())
    work_time = [list(map(int, input().split())) for _ in range(application_count)]
    work_time.sort(key=lambda x: x[1])
    count = 1
    a = work_time[0][1]
    for i in range(len(work_time)):
        if work_time[i][0] >= a:
            a = work_time[i][1]
            count += 1
    print('#{} {}'.format(test_case, count))