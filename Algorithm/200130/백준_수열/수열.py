import sys

sys.stdin = open('input.txt', 'r')

days, sum_days = map(int, input().split())
days_list = list(map(int, input().split()))
result = sum(days_list[0:sum_days])
my_max = result
for i in range(days-sum_days):
    result -= days_list[i]
    result += days_list[i + sum_days]
    if result > my_max:
        my_max = result
print(my_max)
