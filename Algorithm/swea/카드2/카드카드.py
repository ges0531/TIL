import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(range(1, N+1))

while len(numbers) > 1:
    if len(numbers) % 2:
        numbers = [numbers[-1]] + numbers[1:-1:2]
    else:
        numbers = numbers[1::2]

print(numbers[0])