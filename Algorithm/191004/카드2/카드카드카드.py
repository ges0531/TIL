import collections
import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
opt = 1
q = collections.deque()
for i in range(1, N+1):
    q.append(i)
while len(q) != 1:
    if opt == 1:
        q.popleft()
        opt = 0
    elif opt == 0:
        a = q.popleft()
        q.append(a)
        opt = 1
print(q[0])