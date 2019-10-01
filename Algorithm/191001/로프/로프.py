import sys

sys.stdin = open('input.txt', 'r')

lope_count = int(input())
lope_list = [int(input()) for _ in range(lope_count)]
lope_list.sort()
my_max = 0
while lope_list:
    my_num = lope_list[0]*len(lope_list)
    if my_max < my_num:
        my_max = my_num
    lope_list.pop(0)
print(my_max)