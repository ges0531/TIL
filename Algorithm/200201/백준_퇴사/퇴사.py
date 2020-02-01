import sys

sys.stdin = open('input.txt', 'r')


def max_gain(day, gain):
    global my_max
    if day >= work_days:
        if gain > my_max:
            my_max = gain
        return
    if memoization[day] > gain:
        return
    else:
        memoization[day] = gain
    for i in range(day, work_days):
        max_gain(i + work_list[i][0], gain+work_list[i][1])



work_days = int(input())
work_list = [list(map(int, input().split())) for _ in range(work_days)]
my_max = 0
memoization = [0]*work_days
for j in range(work_days):
    if work_list[j][0] + j > work_days:
        work_list[j][1] = 0
max_gain(0, 0)
print(my_max)