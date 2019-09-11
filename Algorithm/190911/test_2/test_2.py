a = '01D06079861D79F99F'
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


for _ in range(11):
    result = 0
    if len(real_result) > 7:
        for i in range(6, -1, -1):
            result += (real_result.pop(0)) * (1<<i)
        else:
            print(result, end=' ')
    else:
        for j in range(len(real_result)-1, -1, -1):
            result += (real_result.pop(0)) * (1<<j)
        else:
            print(result, end=' ')
