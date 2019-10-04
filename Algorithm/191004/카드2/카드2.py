import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

num_list = [i+1 for i in range(N)]
a = [0]
while num_list:
    num_list.pop(0)
    a[0] = num_list.pop(0)
    num_list = num_list + a
print(num_list[0])