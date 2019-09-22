import sys

sys.stdin = open('input.txt', 'r')


def perm_r_4(a, k, n, t, visited):
    global count
    if k == n:
        if count == perm_count-1:
            print(''.join(map(str, t)))
        count += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            t[k] = a[i]
            visited[i] = 1
            if count > perm_count-1:
                return
            perm_r_4(a, k + 1, n, t, visited)
            visited[i] = 0


nums = list(map(int, input().split()))
nums.sort()
perm_count = int(input())
count = 0
length = len(nums)
perm_r_4(nums, 0, length, [0]*length, [0]*length)