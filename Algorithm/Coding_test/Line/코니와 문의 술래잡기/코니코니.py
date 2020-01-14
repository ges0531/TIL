import sys

sys.stdin = open('input_1.txt', 'r')


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y, idx, l):
    l += str(arr[x][y])
    if idx == 7:
        result.add(l)
        return
    else:
        for i in range(4):
            if 0 <= x + dx[i] < len(arr) and 0 <= y + dy[i] < len(arr[0]):
                dfs(x + dx[i], y + dy[i], idx + 1, l)


for tc in range(1, 1 + int(input())):
    print('#%d' % (tc), end=' ')
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            l = ''
            dfs(i, j, 1, l)
    print(result)
    print(len(set(result)))