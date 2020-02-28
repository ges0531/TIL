def comb(arr, t, length, k, r):
    if len(t) > 1:
        if t[k-2] > t[k-1]:
            return
    if len(t) == r:
        print(' '.join(map(str, t)))
        return
    for i in range(k, length):
        if not visited[i]:
            visited[i] = 1
            t.append(arr[i])
            comb(arr, t, length, k+1, r)
            t.pop()
            visited[i] = 0

n, r = map(int, input().split())
visited = [0]*n
comb([i+1 for i in range(n)], [], n, 0, r)
