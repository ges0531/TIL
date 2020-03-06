import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [0] * size
    dx = [0, 0 ,-1, 1]
    dy = [-1, 1, 0, 0]
    stack = []
    top = 0
    count = 0
    print(test_case)
    for s in range(size):
        matrix_column = list(map(int, map(str, input())))
        matrix[s] = matrix_column
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 2:
                stack.append([column, row])
    success = 0
    while success or stack != []:
        back = top
        for d in range(4):
            if stack[top][0] + dy[d] >= 0 and stack[top][0] + dy[d] < size:
                if stack[top][1] + dx[d] >= 0 and stack[top][1] + dx[d] < size:
                    if matrix[stack[top][0] + dy[d]][stack[top][1] + dx[d]] == 0:
                        matrix[stack[top][0] + dy[d]][stack[top][1] + dx[d]] = 1
                        stack.append([stack[top][0] + dy[d], stack[top][1] + dx[d]])
                        top += 1
                    elif matrix[stack[top][0] + dy[d]][stack[top][1] + dx[d]] == 3:
                        success = 1
                        break
        if top == back:
            stack.pop()
            top -= 1
        print(stack)
    if success:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))

        #             if matrix[column][row] == 2:
            #                 if matrix[column+dy[d]][row+dx[d]] == 0:
            #                     matrix[column + dy[d]][row + dx[d]] = 1
            #                     stack.append([column+dy[d], row+dx[d]])
            #                     top += 1
            #                 elif matrix[column+dy[d]][row+dx[d]] == 3:
            #                     print('gg')
            #                     break
            #                 else:



