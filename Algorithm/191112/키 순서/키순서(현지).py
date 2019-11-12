import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    M = int(input())

    node = [[0]*(N+1) for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        node[a][b] = 1

    def bigBFS(n):
        global count, node
        visited = [0]*(N+1)
        visited[n] = 1
        queue = [n]
        while queue:
            temp = queue.pop(0)
            for x in range(1, N+1):
                if node[temp][x] and not visited[temp]:
                    visited[temp] = 1
                    queue.append(temp)
                    count += 1

        visited = [0] * (N + 1)
        queue = [n]
        visited[n] = 1
        while queue:
            temp = queue.pop(0)
            for x in range(1, N+1):
                if node[x][temp] and not visited[x]:
                    visited[x]= 1
                    queue.append(x)
                    count += 1


    result = 0
    for n in range(1, N+1):
        count = 0
        bigBFS(n)
        if count == N-1:
            result += 1

    print('#{} {}'.format(tc, result))