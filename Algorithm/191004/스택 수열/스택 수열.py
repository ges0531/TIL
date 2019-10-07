import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
visited = [0]*N
stack = []
while True:
        for i in range(1, int(input())+1):
            if not visited[i]:
                visited[i] = 1
                stack.append(i)

