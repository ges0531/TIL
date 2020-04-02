import sys


sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    result = []
    ordered_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    case_length = int(input().split()[1])
    unordered_str = list(input().split())
    for i in range(len(ordered_str)):
        for j in range(len(unordered_str)):
            if ordered_str[i] == unordered_str[j]:
                result.append(unordered_str[j])
    print('#{}'.format(test_case))
    print(' '.join(result))
