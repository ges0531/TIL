import sys
sys.stdin = open("input.txt", 'r')

def dfs(selected, v, k):
    global max_cnt
    for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        i = v[0] + di
        j = v[1] + dj
        if 0 <= i <= R-1 and 0 <= j <= C-1 and not(selected[ord(alphabets[i][j])-65]):
            selected[ord(alphabets[i][j])-65] = True
            dfs(selected, [i, j], k + 1)
            selected[ord(alphabets[i][j])-65] = False
    if k > max_cnt:
        max_cnt = k

R, C = map(int, input().split())
max_cnt = 1
alphabets = [input() for _ in range(R)]
sel = [False]*26
sel[ord(alphabets[0][0])-65] = True
dfs(sel, [0, 0], 1)
print(max_cnt)