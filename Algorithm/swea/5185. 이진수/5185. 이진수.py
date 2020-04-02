import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, decimal = input().split()
    decimal = list(decimal)
    real_result = [0]*int(N)
    index_2 = 0
    for i in range(int(N)):
        index = 0
        result = [0]*4
        if decimal[i] == 'A':
            decimal[i] = '10'
        elif decimal[i] == 'B':
            decimal[i] = '11'
        elif decimal[i] == 'C':
            decimal[i] = '12'
        elif decimal[i] == 'D':
            decimal[i] = '13'
        elif decimal[i] == 'E':
            decimal[i] = '14'
        elif decimal[i] == 'F':
            decimal[i] = '15'
        if decimal[i] == '0':
            real_result[index_2] = [0, 0, 0, 0]
            index_2 += 1
        else:
            b = int(decimal[i])
            while b:
                a = b % 2
                b = b // 2
                result[index] = a
                index += 1
            result.reverse()
            real_result[index_2] = result
            index_2 += 1
    c = sum(real_result, [])
    d = ''
    for j in range(len(c)):
        d += str(c[j])

    print('#{} {}'.format(test_case, d))