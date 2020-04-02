def Find_set(x):
    if x == p[x]:
        return x
    else:
        return Find_set(p[x])

def Union(x, y):
    p[Find_set(y)] = Find_set(x)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    p = [i for i in range(N+1)]
    for i in range(M):
        Union(node[i][0], node[i][1])
    cnt = 0
    for i in range(1, N+1):
        if p[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))