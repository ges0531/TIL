import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    string = list(input())
    index = 1
    my_list = []
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            string.pop(i)
            string.pop(i)
            i = 0
            break
        print(string)