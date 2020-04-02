import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    result = []
    matrix_size, length = map(int, input().split())
    word_list = [0] * matrix_size
    for size in range(matrix_size):
        word_list[size] = list(input())
    list_copy = word_list
    palindrome = [0] * length
    for column in range(len(word_list)):
        column_box = [0] * matrix_size
        for row in range(len(word_list[0])):
            column_box[row] = word_list[column][row]
        for index in range(length):
            palindrome[index] = column_box.pop()
        if palindrome == palindrome[::-1]:
            result.append(''.join(palindrome))
    word_list = list_copy
    for row in range(len(word_list[0])):
        row_box = [0] * matrix_size
        for column in range(len(word_list)):
            row_box[column] = word_list[column][row]
        for index in range(length):
            palindrome[index] = row_box.pop()
        if palindrome == palindrome[::-1]:
            result.append(''.join(palindrome))
    print('#{} {}'.format(test_case, result[0]))
