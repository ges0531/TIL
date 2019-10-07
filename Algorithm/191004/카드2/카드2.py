import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

num_list = [i+1 for i in range(N)]
a = [0]
index = 0
for _ in range(N-1):
    index += 1
    a[0] = num_list[index]
    index += 1
    num_list = num_list+a
print(num_list[-1])