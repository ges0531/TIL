import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    a, b = map(str, input().split())
    li = list(map(int, [num for num in a]))
    min_v, min_idex = 10, len(li)-1
    j = 0
    for j in range(int(b)):
        k = j
        if k < len(li):
            idx = j-1
            max_index = j-1
            while max_index == idx and idx < len(li):
                max_v = 0
                cnt = 0
                idx += 1
                for i in range(k, len(li)):
                    if max_v <= li[i]:
                        max_v = li[i]
                        max_index = i
                if k+1 <= int(b):
                    k+=1
            if idx < len(li):
                max_idxes = []
                for ma in range(len(li)):
                    if li[ma] == max_v:
                        cnt += 1
                        max_idxes.append(ma)
                if cnt != 1:
                    ch = sorted(set(li)).index(li[idx])
                    li[max_idxes[::-1][ch]], li[idx] = li[idx], li[max_idxes[::-1][ch]]
                else:
                    if idx < len(li):
                        li[max_index], li[idx] = li[idx], li[max_index]
    if int(b) > len(li):
        for _ in range(int(b) - len(li) +1):
            li[-2], li[-1] = li[-1], li[-2]
    print(int(''.join(map(str, li))))