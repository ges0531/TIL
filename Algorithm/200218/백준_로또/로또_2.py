import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')

while True:
    number_list = list(map(int, input().split()))
    if number_list[0] == 0:
        break
    for i in combinations(number_list[1:], 6):
        print(' '.join(map(str, i)))
    print()