import sys

sys.stdin = open('input.txt', 'r')

change_count = int(input())
change_list = [list(map(int, input().split())) for _ in range(change_count)]
cup_list = [1, 2, 3]
for i in range(change_count):
    a = change_list[i][0]
    b = change_list[i][1]
    c = cup_list.index(b)
    cup_list[cup_list.index(a)] = b
    cup_list[c] = a
print(cup_list[0])