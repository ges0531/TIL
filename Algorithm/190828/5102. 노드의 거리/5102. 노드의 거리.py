import sys


sys.stdin = open('input.txt', 'r')

T = int(input())


def BFS(E, v):
    visited = [0]*(node_count+1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
        for k in range(len(E[t])):
            if not visited[k]:
                if E[t][k] == 1:
                    visited[k] = visited[t]+1
                    queue.append(k)
    if visited[result[1]] == 0:
        print('#{} {}'.format(test_case, visited[result[1]]))
    else:
        print('#{} {}'.format(test_case, visited[result[1]]-1))


for test_case in range(1, T+1):
    node_count, link_count = map(int, input().split())
    links = [list(map(int, input().split())) for _ in range(link_count)]
    result = list(map(int, input().split()))
    G = [[0]*(node_count+1) for _ in range(node_count+1)]
    for i in range(len(links)):
        for j in range(len(links[0])):
            G[links[i][0]][links[i][1]] = 1
            G[links[i][1]][links[i][0]] = 1

    BFS(G, result[0])
