import sys

sys.stdin = open('input.txt', 'r')


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


def BFS(v, visited):
    queue = []
    queue.append(v)
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for i in edges[v]:
                if not visited[i]:
                    queue.append(i)


num_list = list(map(int, input().split()))

edges = [[] for _ in range(len(num_list)//2)]

for k in range(len(num_list)//2):
    edges[num_list[2*k]].append(num_list[2*k+1])
    edges[num_list[2 * k+1]].append(num_list[2 * k])

DFS(1, [0]*8)
print()
BFS(1, [0]*8)
