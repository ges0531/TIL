import sys

sys.stdin = open('input.txt',  'r')


def DFSr(v):  # recursive DFS
    if visited[v] == 0:
        visited[v] = True
        result.append(v)
    for i in range(1, node_count+1):
        if G[v][i] and not visited[i]:
            count = 0
            G[v][i] = 0
            for G_column in range(len(G)):
                if G[G_column][i]:
                    count += 1
            if count == 0:
                DFSr(i)

T = 1

for test_case in range(1, T+1):
    node_count, link_count = map(int, input().split())
    work_order = list(map(int, input().split()))
    G = [[0] * (node_count + 1) for _ in range(node_count + 1)]
    for i in range(len(work_order)//2):
        G[work_order[2*i]][work_order[2*i+1]] = 1
    visited = [0] * (node_count+1)
    result = []
    end_node = [0] * (len(work_order)//2)
    start_node = []
    # for start in range(len(work_order)//2):
    #     DFSr(work_order[2*start])
    for j in range(len(work_order)//2):
        end_node[j] = work_order[2*j+1]
    for k in range(len(work_order)//2):
        if work_order[2*k] not in end_node and work_order[2*k] not in start_node:
            start_node.append(work_order[2*k])
    for start in range(len(start_node)):
        DFSr(start_node[start])
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))


