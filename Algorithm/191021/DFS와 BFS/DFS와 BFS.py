import sys

sys.stdin = open('input.txt', 'r')


def BFS(start):
    global result
    queue = [start]
    visited = [0]*(node_count+1)
    visited[start] = 1
    while queue:
        a = queue.pop(0)
        result.append(a)
        for j in G[a]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)


def DFS(start):
    global result_2
    stack = [start]
    visited = [0]*(node_count+1)
    while stack:
        a = stack.pop()
        visited[a] = 1
        result_2.append(a)
        for jj in G[a]:
            if not visited[jj]:
                stack.append(jj)
                break


node_count, link_count, start_node = map(int, input().split())
link_list = [list(map(int, input().split())) for _ in range(link_count)]
G = [[] for _ in range(node_count+1)]
for i in range(link_count):
    G[link_list[i][0]].append(link_list[i][1])
    G[link_list[i][1]].append(link_list[i][0])
for k in range(len(G)):
    G[k].sort()
result = []
result_2 = []
DFS(start_node)
BFS(start_node)
print(' '.join(map(str, result_2)))
print(' '.join(map(str, result)))
