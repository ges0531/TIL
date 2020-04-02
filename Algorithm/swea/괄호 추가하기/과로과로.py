import sys

sys.stdin = open('input.txt', 'r')


def bracket(k, N, arr):
    if k+3 > N:
        for ii in range(N):
            if ii % 2 == 0:
                string[ii] = str(string[ii])
        result = ''.join(arr)
        result = list(result)
        print(result)

        # for m in range(len(result)):
        #     if result[m] == '+':
        #         result[m+1] = result[m-1]+result[m+1]
        #         arr[i-1] = ''
        #         arr[i] = ''
        #     elif arr[i] == '*':
        #         if type(arr[i + 1]) == int and type(arr[i - 1]) == int:
        #             arr[i + 1] = arr[i - 1] * arr[i + 1]
        #             arr[i - 1] = ''
        #             arr[i] = ''
        #     elif arr[i] == '-':
        #         if type(arr[i + 1]) == int and type(arr[i - 1]) == int:
        #             arr[i + 1] = arr[i - 1] - arr[i + 1]
        #             arr[i - 1] = ''
        #             arr[i] = ''
    else:
        for i in range(k, N-1):
            if arr[i] == '+':
                if type(arr[i+1]) == int and type(arr[i-1]) == int:
                    arr[i+1] = arr[i-1]+arr[i+1]
                    arr[i-1] = ''
                    arr[i] = ''
            elif arr[i] == '*':
                if type(arr[i + 1]) == int and type(arr[i - 1]) == int:
                    arr[i + 1] = arr[i - 1] * arr[i + 1]
                    arr[i - 1] = ''
                    arr[i] = ''
            elif arr[i] == '-':
                if type(arr[i + 1]) == int and type(arr[i - 1]) == int:
                    arr[i + 1] = arr[i - 1] - arr[i + 1]
                    arr[i - 1] = ''
                    arr[i] = ''
            bracket(k+4, N, arr)
            arr[i-1], arr[i], arr[i+1] = copy_string[i-1], copy_string[i], copy_string[i+1]


string_length = int(input())

string = list(input())
for j in range(string_length):
    if j % 2 == 0:
        string[j] = int(string[j])
copy_string = string[:]
bracket(0, string_length, string)