import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size  = int(input())
    farm = [list(map(int, input())) for _ in range(size)]
    my_sum = 0
    k = -1
    for column in range(len(farm)):
        if column <= size//2:
            k += 1
        else:
            k -= 1
        for row in range(len(farm[0])):
            if (size//2)-k <= row <= (size//2)+k:
                my_sum += farm[column][row]
    print('#{} {}'.format(test_case, my_sum))