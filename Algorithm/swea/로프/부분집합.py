import sys

sys.stdin = open('input.txt', 'r')


def comb_r(k, s, n, r, a, t, result=0):
    global my_max
    if k == r:
        if t:
            if my_max < result:
                my_max = result
    else:
        t = [0]*r
        for i in range(s, n + (k - r) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1, n, r, a, t, result + (r * min(t)))


lope_count = int(input())
lope_list = [int(input()) for _ in range(lope_count)]
my_max = 0
for ii in range(lope_count+1):
    comb_r(0, 0, lope_count, ii, lope_list, [0]*ii)
print(my_max)