import sys

sys.stdin = open('input.txt',  'r')


def DFSr(v):  # recursive DFS
    visited[v] = True
    result.append(v)
    for i in range(1, node_count+1):
        if G[v][i] and not visited[i]:
            DFSr(i)

T = int(input())

for test_case in range(1, T+1):
    node_count, link_count = map(int, input().split())
    links = [list(map(int, input().split())) for _ in range(link_count)]
    start_node, last_node = map(int, input().split())
    G = [[0] * (node_count+1) for _ in range(node_count+1)]
    visited = [0] * (node_count+1)
    result = []
    for link in links:
        G[link[0]][link[1]] = 1
    DFSr(start_node)
    if last_node in result:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))