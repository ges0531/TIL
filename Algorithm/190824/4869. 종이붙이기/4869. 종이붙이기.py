import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())//10
    result = 1
    if N % 2:
        for _ in range(N//2):
            result *= 4
            result += 1
    else:
        for _ in range(N//2):
            result *= 4
            result -= 1
    print('#{} {}'.format(test_case, result))
