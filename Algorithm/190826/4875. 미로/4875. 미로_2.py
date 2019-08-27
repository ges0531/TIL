T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [0] * size
    dx = [0, 0 ,-1, 1]
    dy = [-1, 1, 0, 0]
    stack = []
    top = 0
    count = 0
    for s in range(size):
        matrix_column = list(map(int, map(str, input())))
        matrix[s] = matrix_column
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 2:
                stack.append([column, row])
    a = 0
    while a != 10:
        back = top
        for d in range(4):
            if stack[top][0] + dy[d] >= 0 and stack[top][0] + dy[d] < size:
                if stack[top][1] + dx[d] >= 0 and stack[top][1] + dx[d] < size:
                    if matrix[stack[top][0] + dy[d]][stack[top][1] + dx[d]] == 0:
                        matrix[stack[top][0] + dy[d]][stack[top][1] + dx[d]] = 1
                        stack.append([stack[top][0] + dy[d], stack[top][1] + dx[d]])
                        top += 1
                    elif matrix[stack[top][0] + dy[d]][stack[top][1] + dx[d]] == 3:
                        print('#{} 1'.format(test_case))
                        a = 10
        if top == back:
            stack.pop()
            top -= 1
        if stack == []:
            print('#{} 0'.format(test_case))
            break