import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node, end_node):
    global visited
    queue = [start_node]
    while queue:
        a = queue.pop(0)
        if not visited[a]:
            visited[a] = 1
            for j in range(1, len(link_list[a])):
                if not visited[link_list[a][j]-1]:
                    queue.append(link_list[a][j]-1)


def comb(n, r, arr, t):
    global result, visited
    if r == 0:
        print(t)
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)


area_count = int(input())
people_list = list(map(int, input().split()))
link_list = [list(map(int, input().split())) for _ in range(area_count)]
index_list = [k for k in range(area_count)]
for i in range(1, area_count+1):
    result = []
    visited = [0] * area_count
    