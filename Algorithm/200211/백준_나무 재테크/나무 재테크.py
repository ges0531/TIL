import sys

sys.stdin = open('input.txt', 'r')

matrix_size, tree_count, year_count = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
tree_list = [list(map(int, input().split())) for _ in range(tree_count)]
tree_matrix = [[[0]]*matrix_size for _ in range(matrix_size)]
for tr in range(tree_count):
    tree_matrix[tree_list[tr][0]][tree_list[tr][1]] = [tree_list[tr][2]]
print(tree_matrix)