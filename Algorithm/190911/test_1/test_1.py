import sys

sys.stdin = open('input.txt', 'r')

bit = list(input().split())
for i in range(len(bit)):
    bit[i] = list(bit[i])
bit = sum(bit, [])
bit = list(map(int, bit))
for _ in range(10):
    result = 0
    for i in range(6, -1, -1):
        result += int(bit.pop(0)) * (1<<i)
    else:
        print(result, end=' ')
