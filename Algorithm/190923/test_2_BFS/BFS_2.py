import sys

sys.stdin = open('input.txt', 'r')


def BFS(v, visited):
    queue = []
    queue.append(v)
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in edges[v]:
                if not visited[w]:
                    queue.append(w)





num_list = list(map(int, input().split()))

edges = [[] for _ in range(8)]

for j in range(len(num_list)//2):
    edges[num_list[2*j]].append(num_list[2*j+1])
    edges[num_list[2 * j+1]].append(num_list[2 * j])
BFS(1, [0]*8)