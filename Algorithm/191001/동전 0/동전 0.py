import sys

sys.stdin = open('input.txt', 'r')

coin_count, coin_sum = map(int, input().split())

coin = [int(input()) for _ in range(coin_count)]
coin_list = []
count = 0
for i in range(coin_count):
    if coin[i] <= coin_sum:
        coin_list.append(coin[i])
while coin_sum:
    if coin_sum - coin_list[-1] >= 0:
        coin_sum -= coin_list[-1]
        count += 1
    else:
        coin_list.pop(-1)
print(count)