import sys
# by 숙경

sys.stdin = open('input.txt', 'r')

def inorder(n):
    global num
    if edges[n][1]:
        inorder(edges[n][1])
    edges[n][0] = num
    num += 1
    if edges[n][2]:
        inorder(edges[n][2])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    edges = [[0, 0, 0] for _ in range(N+1)]
    for i in range(1, len(edges)):
        if i*2 <= N:
            edges[i][1] = i*2
        if i*2+1 <= N:
            edges[i][2] = i*2 + 1
    print(edges)
    num = 1
    inorder(1)
    print('#%d %d %d' % (tc, edges[1][0], edges[N//2][0]))