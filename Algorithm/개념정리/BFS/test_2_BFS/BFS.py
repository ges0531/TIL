import sys

sys.stdin = open('input.txt', 'r')


def BFS(v, visited):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for i in range(len(edges[t])):
            u = edges[t][i]
            if not visited[u]:
                queue.append(u)
                visited[u] = 1





num_list = list(map(int, input().split()))

edges = [[] for _ in range(8)]

for j in range(len(num_list)//2):
    edges[num_list[2*j]].append(num_list[2*j+1])
    edges[num_list[2 * j+1]].append(num_list[2 * j])
BFS(1, [0]*8)