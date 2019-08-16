import sys
sys.stdin = open('input.txt', 'r')

x = 0
while x != -1:
    x = int(input())
    if x % 3 == 0:
        print(x // 3)

