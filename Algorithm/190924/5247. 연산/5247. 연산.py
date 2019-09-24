import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


def BFS(v):
    queue = deque([v])
    visited = [0]*1000001
    visited[v] = 1
    while queue:
        a = queue.popleft()
        if a == max_num:
            return visited[a]-1
        if a + 1 <= 1000000:
            if not visited[a+1]:
                queue.append(a+1)
                visited[a+1] = visited[a]+1
        if 0 < a-1:
            if not visited[a-1]:
                    queue.append(a - 1)
                    visited[a-1] = visited[a] + 1
        if a * 2 <= 1000000:
            if not visited[a*2]:
                queue.append(a*2)
                visited[a*2] = visited[a] + 1
        if a-10 > 0:
            if not visited[a-10]:
                queue.append(a-10)
                visited[a-10] = visited[a] + 1


T = int(input())

for test_case in range(1, T+1):
    small_num, max_num = map(int, input().split())
    print('#{} {}'.format(test_case, BFS(small_num)))