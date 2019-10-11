import sys

sys.stdin = open('input.txt', 'r')

string_length = int(input())

string = list(input())
count = 0
for i in range(string_length):
    if string[i] == '+':
        if i+2 < len(string):
            if string[i+2] == '+':
                string[i + 2] = '++'
        string[i] = int(string[i - 1]) + int(string[i + 1])
        string[i + 1] = 0
        string[i - 1] = 0
        count += 2
for ii in range(count):
    if 0 in string:
        string.remove(0)
print(string)
for j in range(len(string)):
    if string[j] == '++':
        string[j + 1] = int(string[j - 1]) + int(string[j + 1])
        string[j] = 0
        string[j - 1] = 0
    elif string[j] == '*':
        string[j+1] = int(string[j-1])*int(string[j+1])
        string[j] = 0
        string[j - 1] = 0
    elif string[j] == '-':
        if j+2 < len(string):
            if string[j+2] == '-':
                if j+3 < len(string):
                    if int(string[j+1]) < int(string[j+3]):
                        string[j+3] = int(string[j+3]) - int(string[j+1])
                        string[j + 1] = 0
                        string[j] = 0
                        string[j+2] = 0
        string[j + 1] = int(string[j - 1]) - int(string[j + 1])
        string[j] = 0
        string[j - 1] = 0
print(string)