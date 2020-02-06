import sys

sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    clap_list = list(map(int, input()))
    result = clap_list[0]
    i = 1
    people = 0
    while i < len(clap_list):
        if i <= result:
            result += clap_list[i]
            i += 1
        else:
            people += 1
            result += 1
    print('#{} {}'.format(test_case, people))