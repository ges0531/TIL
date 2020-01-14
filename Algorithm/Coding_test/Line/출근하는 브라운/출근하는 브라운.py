import sys

sys.stdin = open('input.txt', 'r')

seat_count = int(input())
seat_list = list(map(int, input().split()))
count = 0
count_list = []
for i in range(seat_count):
    if seat_list[i] == 0:
        count += 1
    else:
        count_list.append(count)
        count = 0
a = max(count_list)
if a % 2:
    print((a//2)+1)
else:
    print(a//2)
