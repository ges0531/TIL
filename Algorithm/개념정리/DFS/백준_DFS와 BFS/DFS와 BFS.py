import sys

sys.stdin = open('input.txt', 'r')


def DFS(flag_node):
    global visited
    print(flag_node, end=' ')
    for j in range(len(my_list[flag_node])):
        if not visited[my_list[flag_node][j]]:
            visited[my_list[flag_node][j]] = 1
            DFS(my_list[flag_node][j])


def BFS(flag_node):
    global my_list
    queue = [flag_node]
    visited_2 = [0]*(node_count+1)
    visited_2[flag_node] = 1
    while queue:
        a = queue.pop(0)
        print(a, end=' ')
        for k in range(len(my_list[a])):
            if not visited_2[my_list[a][k]]:
                visited_2[my_list[a][k]] = 1
                queue.append(my_list[a][k])



node_count, line_count, start_node = map(int, input().split())
node_list = [list(map(int, input().split())) for _ in range(line_count)]
my_list = [[] for _ in range(node_count+1)]
for i in node_list:
    my_list[i[0]].append(i[1])
    my_list[i[1]].append(i[0])
for ii in range(node_count+1):
    my_list[ii].sort()
visited = [0]*(node_count+1)
visited[start_node] = 1
DFS(start_node)
print()
BFS(start_node)