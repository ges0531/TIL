import sys, itertools

sys.stdin = open('input.txt', 'r')


def perm(k, n, arr, visited, t, r):
    if k == r:
        print(' '.join(map(str, t)))
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                t.append(arr[i])
                perm(k+1, n, arr, visited, t, r)
                t.pop()
                visited[i] = 0

def perm_2(k, n, arr):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm_2(k+1, n, arr)
            arr[i], arr[k] = arr[k], arr[i]


N, M = map(int, input().split())
# perm(0, N, [i+1 for i in range(N)], [0]*N, [], M)
# perm_2(0, N, [i+1 for i in range(N)])
print(list(itertools.product([i+1 for i in range(N)], repeat=2)))
print(list(itertools.permutations([i+1 for i in range(N)])))
print(list(itertools.combinations([i+1 for i in range(N)], 2)))
print(list(itertools.combinations_with_replacement([i+1 for i in range(N)], 2)))
