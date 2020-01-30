import sys

sys.stdin = open('input.txt', 'r')

def search_moon(start_node, count, key_dict):
    global my_min
    y = start_node[0]
    x = start_node[1]
    if matrix[y][x] == '1':
        my_min = count
        return
    if count > my_min:
        return
    for i in range(4):
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
            if not visited[idy][idx]:
                if not matrix[idy][idx] == '#':
                    if matrix[idy][idx] == 'a':
                        key_dict['a'] += 1
                        matrix[idy][idx] = '.'
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count+1, key_dict)
                        visited[idy][idx] = 0
                        matrix[idy][idx] = 'a'
                        key_dict['a'] -= 1
                    elif matrix[idy][idx] == 'A':
                        if key_dict['a']:
                            key_dict['a'] -= 1
                            matrix[idy][idx] = '.'
                            visited[idy][idx] = 1
                            search_moon([idy, idx], count+1, key_dict)
                            visited[idy][idx] = 0
                            matrix[idy][idx] = 'A'
                            key_dict['a'] += 1
                    elif matrix[idy][idx] == 'b':
                        key_dict['b'] += 1
                        matrix[idy][idx] = '.'
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count+1, key_dict)
                        visited[idy][idx] = 0
                        matrix[idy][idx] = 'b'
                        key_dict['b'] -= 1
                    elif matrix[idy][idx] == 'B':
                        if key_dict['b']:
                            key_dict['b'] -= 1
                            matrix[idy][idx] = '.'
                            visited[idy][idx] = 1
                            search_moon([idy, idx], count+1, key_dict)
                            visited[idy][idx] = 0
                            matrix[idy][idx] = 'B'
                            key_dict['b'] += 1
                    elif matrix[idy][idx] == 'c':
                        key_dict['c'] += 1
                        matrix[idy][idx] = '.'
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count+1, key_dict)
                        visited[idy][idx] = 0
                        matrix[idy][idx] = 'c'
                        key_dict['c'] -= 1
                    elif matrix[idy][idx] == 'C':
                        if key_dict['c']:
                            key_dict['c'] -= 1
                            matrix[idy][idx] = '.'
                            visited[idy][idx] = 1
                            search_moon([idy, idx], count+1, key_dict)
                            visited[idy][idx] = 0
                            matrix[idy][idx] = 'C'
                            key_dict['c'] += 1
                    elif matrix[idy][idx] == 'd':
                        key_dict['d'] += 1
                        matrix[idy][idx] = '.'
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count+1, key_dict)
                        visited[idy][idx] = 0
                        matrix[idy][idx] = 'd'
                        key_dict['d'] -= 1
                    elif matrix[idy][idx] == 'D':
                        if key_dict['d']:
                            key_dict['d'] -= 1
                            matrix[idy][idx] = '.'
                            visited[idy][idx] = 1
                            search_moon([idy, idx], count+1, key_dict)
                            visited[idy][idx] = 0
                            matrix[idy][idx] = 'D'
                            key_dict['d'] += 1
                    elif matrix[idy][idx] == 'e':
                        key_dict['e'] += 1
                        matrix[idy][idx] = '.'
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count+1, key_dict)
                        visited[idy][idx] = 0
                        matrix[idy][idx] = 'e'
                        key_dict['e'] -= 1
                    elif matrix[idy][idx] == 'E':
                        if key_dict['e']:
                            key_dict['e'] -= 1
                            matrix[idy][idx] = '.'
                            visited[idy][idx] = 1
                            search_moon([idy, idx], count+1, key_dict)
                            visited[idy][idx] = 0
                            matrix[idy][idx] = 'E'
                            key_dict['e'] += 1
                    elif matrix[idy][idx] == 'f':
                        key_dict['f'] += 1
                        matrix[idy][idx] = '.'
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count+1, key_dict)
                        visited[idy][idx] = 0
                        matrix[idy][idx] = 'f'
                        key_dict['f'] -= 1
                    elif matrix[idy][idx] == 'F':
                        if key_dict['f']:
                            key_dict['f'] -= 1
                            matrix[idy][idx] = '.'
                            visited[idy][idx] = 1
                            search_moon([idy, idx], count+1, key_dict)
                            visited[idy][idx] = 0
                            matrix[idy][idx] = 'F'
                            key_dict['f'] += 1
                    else:
                        visited[idy][idx] = 1
                        search_moon([idy, idx], count + 1, key_dict)
                        visited[idy][idx] = 0


matrix_column, matrix_row = map(int, input().split())

matrix = [list(input()) for _ in range(matrix_column)]
key_dictionary = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
visited = [[0]*matrix_row for _ in range(matrix_column)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
start = []
my_min = 1000000
for column in range(matrix_column):
    for row in range(matrix_row):
        if matrix[column][row] == '0':
            start = [column, row]
search_moon(start, 0, key_dictionary)
if my_min == 1000000:
    print(-1)
else:
    print(my_min)