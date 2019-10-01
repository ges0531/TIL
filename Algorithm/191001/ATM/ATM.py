import sys

sys.stdin = open('input.txt', 'r')

people_count = int(input())
people_time = list(map(int, input().split()))
people_time.sort()
my_sum = 0
result = 0
for i in range(people_count):
    my_sum += people_time[i]
    result += my_sum

print(result)