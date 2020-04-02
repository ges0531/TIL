import itertools

def perm(arr, t, length):
    if len(t) == n:
        print(t)
        return
    for i in range(length):
        if not visited[i]:
            visited[i] = 1
            t.append(arr[i])
            perm(arr, t, length)
            t.pop()
            visited[i] = 0

def comb(arr, t, length, k, r):
    if len(t) > 1:
        if t[k-2] > t[k-1]:
            return
    if len(t) == r:
        print(t)
        return
    for i in range(k, length):
        if not visited[i]:
            visited[i] = 1
            t.append(arr[i])
            comb(arr, t, length, k+1, r)
            t.pop()
            visited[i] = 0

def comb_2(arr, t, n, r):
    if r == 0:
        print(t)
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb_2(arr, t, n-1, r-1)
        comb_2(arr, t, n-1, r)


my_list = [1, 2, 3, 4, 5]
n = len(my_list)
visited = [0]*n
# perm(my_list, [], n)
# comb(my_list, [], n, 0, 4)
comb_2(my_list, [0]*3, len(my_list), 3)