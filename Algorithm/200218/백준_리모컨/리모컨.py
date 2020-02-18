import sys

sys.stdin = open('input.txt', 'r')


def up_broken(number, count):
    global up_count
    if number == 0:
        up_count = 1000000000
        return
    if number in broken_list:
        up_broken(number+1, count+1)
    else:
        up_count = count
        return


def down_broken(number, count):
    global down_count
    if number == 0:
        down_count = 1000000000
        return
    if number in broken_list:
        down_broken(number-1, count+1)
    else:
        down_count = count
        return

channel = list(map(int, input()))
broken_count = int(input())
broken_list = list(map(int, input().split()))
flag_count = len(channel)
result = 0
for i in channel:
    up_count = 0
    down_count = 0
    flag_count -= 1
    if i in broken_list:
        up_broken(i, 0)
        down_broken(i, 0)
        if up_count < down_count:
            result += up_count*(10**flag_count)
            result += 1
        else:
            result += down_count * (10 ** flag_count)
            result += 1
    else:
        result += 1
print(result)
