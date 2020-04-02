import sys
# by 재평이형
sys.stdin = open('input.txt', 'r')

def inorder(tree, cur):
    global num
    if cur <= N:
        left, right = 2 * cur, 2 * cur + 1
        inorder(tree, left)
        tree[cur] = num
        num += 1
        inorder(tree, right)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    inorder(tree, 1)

    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))