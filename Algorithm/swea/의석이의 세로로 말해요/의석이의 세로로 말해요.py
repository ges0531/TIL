import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    string = [list(input()) for _ in range(5)]
    result = []
    len_max = len(string[0])
    for i in string:
        if len(i) > len_max:
            len_max = len(i)
    word_list = [['']*len_max for _ in range(len(string))]
    for k in range(len(string)):
        for j in range(len(string[k])):
            word_list[k][j] = string[k][j]
    for row in range(len(word_list[0])):
        for column in range(len(word_list)):
            result.append(word_list[column][row])

    print('#{} {}'.format(test_case, ''.join(result)))