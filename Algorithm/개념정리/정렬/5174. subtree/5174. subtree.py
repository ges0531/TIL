import sys

sys.stdin = open('input.txt', 'r')


def preorder_traverse(T):
    global cnt
    cnt += 1
    if T:
        try:
            preorder_traverse(result_link[T][0])
            preorder_traverse(result_link[T][1])
        except IndexError:
            pass

T = int(input())

for test_case in range(1, T+1):
    link_count, start_node = map(int, input().split())
    link_nodes = list(map(int, input().split()))
    link_node = [0]*link_count
    head_node = [0]*link_count
    end_node = []
    result_link = [0]*(link_count+2)
    cnt = 0
    for i in range(link_count):
        link_node[i] = [link_nodes[2*i], link_nodes[2*i+1]]
    for j in range(link_count):
        head_node[j] = link_node[j][0]
    for k in range(1, link_count+2):
        if k not in head_node:
            end_node.append(k)

    for link_1 in range(1, link_count + 2):
        result = []
        for link_2 in range(link_count):
            if link_1 == link_node[link_2][0]:
                result.append(link_node[link_2][1])
        result_link[link_1] = result
    result_link[0] = []
    preorder_traverse(start_node)
    print('#{} {}'.format(test_case, cnt))