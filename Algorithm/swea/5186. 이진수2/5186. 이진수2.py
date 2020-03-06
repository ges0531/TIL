import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    num = input()
    print(num)
    a = 1
    while num != a:
        a += a / 2
        if a >= 1:
            a -= 1
        else:
            if a 
