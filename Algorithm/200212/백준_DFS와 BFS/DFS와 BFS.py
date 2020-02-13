import sys

sys.stdin = open('input.txt', 'r')

def DFS(stack):
    a = stack.pop()
    visited[a] = 1
    print(a)
    for i in range(line_count):
        for j in range(2):
            if not visited[node_list[i][j]]:
                stack.append(node_list[i][j])
                DFS(stack)

def BFS(queue):
    while queue:
        b = queue.pop(0)
        print(b)
        for i in range(line_count):
            for j in range(2):
                if not visited_2[node_list[i][j]]:
                    visited_2[node_list[i][j]] = 1
                    queue.append(node_list[i][j])


node_count, line_count, start_node = map(int, input().split())
node_list = [list(map(int, input().split())) for _ in range(line_count)]
visited = [0]*(node_count+1)
DFS([start_node])
visited_2 = [0]*(node_count+1)
BFS([start_node])