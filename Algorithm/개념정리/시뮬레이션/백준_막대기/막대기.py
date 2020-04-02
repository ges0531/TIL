import sys

sys.stdin = open('input.txt', 'r')

x = int(input())
stick_list = [64]
while sum(stick_list) - x:
    if sum(stick_list) > x:
        stick_list[stick_list.index(min(stick_list))] = min(stick_list)//2
        if sum(stick_list) < x:
            stick_list.append(min(stick_list))
print(len(stick_list))