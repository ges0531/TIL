import sys

sys.stdin = open('input.txt', 'r')

date = int(input())

consult_list = [list(map(int, input().split())) for _ in range(date)]
consult_date = [0] * date
consult_cost = [0] * date

for i in range(len(consult_list)):
    consult_date[i] = consult_list[i][0]
    consult_cost[i] = consult_list[i][1]

