import sys

sys.stdin = open('input.txt', 'r')

def perm(k, n, r):
    global result
    if k == r:
        result.append(num_list[:r])
    else:
        for i in range(k, n):
            num_list[k], num_list[i] = num_list[i], num_list[k]
            perm(k+1, n, r)
            num_list[k], num_list[i] = num_list[i], num_list[k]


num_1, num_2 = map(int, input().split())

num_list = [i+1 for i in range(num_1)]
result = []
perm(0, len(num_list), 2)
result.sort()
for j in result:
    print(' '.join(map(str, j)))
