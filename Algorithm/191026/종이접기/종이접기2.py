import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
m = (2**n)-1

my_list = [2]*m
a = [0, 0, 1]
count = 2
if n == 1:
    print([0])
elif n == 2:
    print(a)
else:
    while n - count:
        b = a[:]
        a.reverse()
        for i in range(len(a)):
            if a[i] == 0:
                a[i] = 1
            else:
                a[i] = 0
        a = b+[0]+a
        count += 1
    print(a)