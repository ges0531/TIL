import sys

sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10000)
def DFS(start_node):
    global visited
    for k in range(len(link_node[start_node])):
        if not visited[link_node[start_node][k]]:
            visited[link_node[start_node][k]] = 1
            DFS(link_node[start_node][k])


node_count, link_count = map(int, input().split())

link_list = [list(map(int, input().split())) for _ in range(link_count)]
link_node = [[] for _ in range(node_count+1)]
visited = [0]*(node_count+1)
count = 0
for i in range(link_count):
    link_node[link_list[i][0]].append(link_list[i][1])
    link_node[link_list[i][1]].append(link_list[i][0])
for j in range(1, node_count+1):
    if not visited[j]:
        visited[j] = 1
        count += 1
        DFS(j)
print(count)