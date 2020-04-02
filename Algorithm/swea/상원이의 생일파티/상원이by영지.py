import sys
sys.stdin = open('input.txt', 'r')


def bfs(v):
    global cnt
    visited = [0] * (n + 1)
    queue = [v]
    visited[v] = 1
    while queue:
        cnt += 1
        for d in range(len(queue)):
            v = queue.pop(0)
            if friends[v]:
                for j in friends[v]:
                    if not visited[j]:
                        queue.append(j)
                        visited[j] = 1
            else:
                return 0
        if cnt == 2:
            return sum(visited)-1


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    friends = [[] for _ in range(n+1)]
    for i in range(m):
        friends[arr[i][0]].append(arr[i][1])
        friends[arr[i][1]].append(arr[i][0])
    cnt = 0
    print('#{} {}'.format(tc, bfs(1)))