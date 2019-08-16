import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

my_min = T[0]

for num in T:
    if num < my_min:
        my_min = num
print(my_min)