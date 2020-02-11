import sys

sys.stdin = open('input.txt', 'r')

matrix_size, tree_count, year_count = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
tree_list = [list(map(int, input().split())) for _ in range(tree_count)]

food_matrix = [[5]*matrix_size for _ in range(matrix_size)]  # 처음 양분 5
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

flag = 0
while year_count - flag:
    dead_list = []
    # 봄
    for i in range(len(tree_list)-1, -1, -1):
        if food_matrix[tree_list[i][0]-1][tree_list[i][1]-1] >= tree_list[i][2]:
            food_matrix[tree_list[i][0]-1][tree_list[i][1]-1] -= tree_list[i][2]
            tree_list[i][2] += 1
        else:
            dead_list.append(tree_list[i])
            tree_list.pop(i)
    # 여름
    for de in range(len(dead_list)):
        food_matrix[dead_list[de][0]-1][dead_list[de][1]-1] += (dead_list[de][2]//2)

    # 가을
    for tr in range(len(tree_list)):
        if tree_list[tr][2] % 5 == 0:
            for k in range(8):
                if 0 <= tree_list[tr][0]+dy[k]-1 < matrix_size and 0 <= tree_list[tr][1]+dx[k]-1 < matrix_size:
                    tree_list.append([tree_list[tr][0]+dy[k], tree_list[tr][1]+dx[k], 1])
    # 겨울
    for breed_1 in range(matrix_size):
        for breed_2 in range(matrix_size):
            food_matrix[breed_1][breed_2] += matrix[breed_1][breed_2]
    flag += 1

print(len(tree_list))

