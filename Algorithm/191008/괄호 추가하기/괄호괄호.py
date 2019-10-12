import sys

sys.stdin = open('input.txt', 'r')


def bracket(k, num_list, operator_list, copy_list):
    global my_max
    if k+1 > string_length:
        print(num_list)
        if my_max < num_list[-1]:
            my_max = num_list[-1]
        return
    else:
        for j in range(k, len(operator_list)):
            if operator_list[j] == '+':
                num_list[j+1] = num_list[j]+num_list[j+1]
            elif operator_list[j] == '*':
                num_list[j+1] = num_list[j] * num_list[j+1]
            elif operator_list[j] == '-':
                num_list[j+1] = num_list[j] - num_list[j+1]
            print(num_list)
            bracket(k + 2, num_list, operator_list, copy_list)
            for a in range(k, len(operator_list)):
                if operator_list[a] == '+':
                    num_list[a + 1] = num_list[a] + num_list[a + 1]
                elif operator_list[a] == '*':
                    num_list[a + 1] = num_list[a] * num_list[a + 1]
                elif operator_list[j] == '-':
                    num_list[a + 1] = num_list[j] - num_list[j + 1]
            num_list[j+1] = copy_list[j+1]


string_length = int(input())

string = list(input())
for i in range(string_length):
    if i % 2 == 0:
        string[i] = int(string[i])
copy = []
operator_list = []
num_list = []
for jj in range(string_length):
    if type(string[jj]) == int:
        num_list.append(string[jj])
    else:
        operator_list.append(string[jj])
for ii in num_list:
    copy += [ii]
my_max = 0
bracket(0, num_list, operator_list, copy)
print(my_max)
