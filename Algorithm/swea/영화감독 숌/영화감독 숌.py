import sys

sys.stdin = open('input.txt', 'r')

num = int(input())
end_num = '666'
count = 0
num_2 = 0
while count < num:
    num_2 += 1
    if end_num in str(num_2):
        count += 1
print(num_2)

