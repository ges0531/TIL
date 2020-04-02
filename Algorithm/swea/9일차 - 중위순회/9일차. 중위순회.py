import sys

sys.stdin = open('input.txt', 'r')


def preorder_traverse(T):
    if T:
        try:
            preorder_traverse(link_node[T][0])
        except IndexError:
            pass
        ans.append(node[T-1][1])
        try:
            preorder_traverse(link_node[T][1])
        except IndexError:
            pass

T = 10

for test_case in range(1, T+1):
    node_count = int(input())
    node = [list(input().split()) for _ in range(node_count)]
    link_node = [0]*(node_count+1)
    ans = []
    for i in range(node_count):
        result = []
        for j in range(2, len(node[i])):
            result.append(int(node[i][j]))
        link_node[i+1] = result
    link_node[0] = []
    preorder_traverse(1)
    print('#{} {}'.format(test_case, ''.join(ans)))