import collections
import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
num_list = collections.deque()
for i in range(1, N+1):
    num_list.append(i)

while len(num_list) != 1:
    num_list.popleft()
    num_list.append(num_list.popleft())
print(num_list[0])

