import sys

sys.stdin = open("input.txt", "r")

integer = int(input())
sum_integer = 0
if integer > 0 and integer < 100:
    while integer != 0:
        sum_integer += integer
        integer -= 1
print(sum_integer)