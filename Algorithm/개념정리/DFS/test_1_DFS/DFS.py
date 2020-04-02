import sys

sys.stdin = open('input.txt', 'r')


def dfsr(v, visited):
    visited[v] = 1
    print(v, end=' ')
    for w in edges[v]:
        if not visited[w]:
            dfsr(w, visited)


def DFS(v, visited):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in edges[v]:
                if not visited[w]:
                    stack.append(w)


num_list = list(map(int, input().split()))

edges = [[] for i in range(8)]
while num_list:  # 쌍방향 정점 만들기
    x = num_list.pop()
    y = num_list.pop()
    edges[x].append(y)
    edges[y].append(x)

DFS(1, [0] * 8)
print('--')
dfsr(1, [0] * 8)