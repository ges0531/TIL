import sys

sys.stdin = open('input.txt', 'r')

password = list(input().split())

a = '0DEC'
a = list(a)
real_result = [0]*len(a)
index_2 = 0
for i in range(len(a)):
    index = 0
    result = [0]*4
    if a[i] == 'A':
        a[i] = '10'
    elif a[i] == 'B':
        a[i] = '11'
    elif a[i] == 'C':
        a[i] = '12'
    elif a[i] == 'D':
        a[i] = '13'
    elif a[i] == 'E':
        a[i] = '14'
    elif a[i] == 'F':
        a[i] = '15'
    if a[i] == '0':
        real_result[index_2] = [0, 0, 0, 0]
        index_2 += 1
    else:
        while a[i]:
            result[index] = int(a[i]) % 2
            a[i] = int(a[i])//2
            index += 1
        result.reverse()
        real_result[index_2] = result
        index_2 += 1
real_result = sum(real_result, [])

for j in range(len(real_result)-1, -1, -1):
    if real_result[j] == 1:
        real_result[j-5]+real_result[j-4]+real_result[j-3]+real_result[j-2]+real_result[j-1]+real_result[j]
