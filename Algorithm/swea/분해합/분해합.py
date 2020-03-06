import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

for i in range(N):
    if (i + sum(list(map(int, str(i))))) == N:
        print(i)
        break
else:
    print(0)
