import sys

sys.stdin = open('input.txt', 'r')


def inorder(tree, cur, N):
    global num
    if cur <= N:
        left, right = cur*2, cur*2+1
        inorder(tree, left, N)
        tree[cur] = num
        num += 1
        inorder(tree, right, N)


T = int(input())

for test_case in range(1, T+1):
    node_count = int(input())
    node = [i+1 for i in range(node_count)]
    num = 1
    N = len(node)
    tree = [0]*(N+1)
    inorder(tree, 1, N)
    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))