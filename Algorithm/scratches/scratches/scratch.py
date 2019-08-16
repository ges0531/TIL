import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))
my_sum = 0
for num in T:
    my_sum += num
my_avr = my_sum//len(T)
print('sum : {}'.format(my_sum))
print('avg : {}'.format(my_avr))