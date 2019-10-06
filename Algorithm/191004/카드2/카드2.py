import sys

sys.stdin = open('input.txt', 'r')

num_list = list(range(1, int(input())+1))
while len(num_list) > 1:
    num_list = num_list[2:] + [num_list[1]]
print(num_list[0])