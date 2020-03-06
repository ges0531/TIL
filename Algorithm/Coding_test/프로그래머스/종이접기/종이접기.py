import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
m = (2**n)-1
k = (2**n)-1
my_list = [2]*m

while m:
    my_list[m // 2] = 0
    for i in range(m):
        if my_list[i] == 2:
            if i > m//2:
                my_list[i] = 1
    for j in range(1, (k // 2) + 1):
        if my_list[(k // 2) - j] == my_list[(k // 2) + j]:
            my_list[(k // 2) + j] = 0
    m = m//2
    print(my_list)
    print()

print(my_list)

