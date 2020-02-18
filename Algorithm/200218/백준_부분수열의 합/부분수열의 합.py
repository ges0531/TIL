import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')




number_count, number_sum = map(int, input().split())
number_list = list(map(int, input().split()))
count = 0
for i in range(number_count):
    for j in combinations(number_list, i+1):
        if sum(j) == number_sum:
            count += 1
print(count)