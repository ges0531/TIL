import sys

sys.stdin = open('input.txt',  'r')


def push(x):
    global top
    top += 1
    stack[top] = x


def pop():
    global top
    if top == -1:
        return 0
    x = stack[top]
    top -= 1
    return x


def findnext(v):
    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            return i
    return 0


def DFS(v):
    global result
    visited[v] = True
    result.append(v)
    while v:
        w = findnext(v)
        if w:
            push(v)
        while w:
            visited[w] = True
            result.append(w)
            push(w)
            v = w
            w = findnext(v)
        v = pop()



T = 1

for test_case in range(1, T+1):
    node_count, link_count = map(int, input().split())
    work_order = list(map(int, input().split()))
    visited = [0] * (node_count+1)
    G = [[0] * (node_count+1) for _ in range(node_count+1)]
    for i in range(len(work_order)//2):
        G[work_order[2*i]][work_order[2*i+1]] = 1
    stack = [0] * 100
    top = -1
    end_node = [0] * (len(work_order) // 2)
    start_node = []
    result = []
    for j in range(len(work_order) // 2):
        end_node[j] = work_order[2 * j + 1]
    for k in range(len(work_order) // 2):
        if work_order[2 * k] not in end_node and work_order[2 * k] not in start_node:
            start_node.append(work_order[2 * k])
    for start in range(len(start_node)):
        DFS(start_node[start])
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))