import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size, count = map(int, input().split())
    matrix = [0] * size
    print(test_case)
    rec_box = [0] * 2
    black = 0
    for i in range(size):
        matrix[i] = [0]*size
    for _ in range(count):
        rectangles = list(map(int, input().split()))
        for i in range(2):
            rec_box[i] = [rectangles[2*i], rectangles[2*i + 1]]
        for column in range(rec_box[0][0], rec_box[1][0]+1):
            for row in range(rec_box[0][1], rec_box[1][1]+1):
                if matrix[column][row] == 0:
                    matrix[column][row] = 1
                    black += 1
    print('#{} {}'.format(test_case, black))

