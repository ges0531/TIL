import sys

sys.stdin = open('input.txt', 'r')


def DFS(flag_node):
    # print(flag_node, end=' ')
    for j in range(len(my_list[flag_node])):
        if not visited[jj]:
            visited[jj] = 1
            DFS(jj)

def BFS(flag_node):
    queue = [flag_node]
    visited_2 = [0]*(node_count+1)
    visited_2[flag_node] = 1
    while queue:
        a = queue.pop(0)
        print(a, end=' ')
        for k in my_list[a]:
            for kk in [k]:
                if not visited_2[kk]:
                    visited_2[kk] = 1
                    queue.append(kk)



node_count, line_count, start_node = map(int, input().split())
node_list = [list(map(int, input().split())) for _ in range(line_count)]
my_list = [[] for _ in range(node_count+1)]
for i in node_list:
    my_list[i[0]].append(i[1])
    my_list[i[1]].append(i[0])
for ii in range(line_count):
    my_list[ii].sort()
visited = [0]*(node_count+1)
visited[start_node] = 1
DFS(start_node)
# print()
# BFS(start_node)