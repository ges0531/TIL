import sys

sys.stdin = open('input.txt', 'r')





T = int(input())
T = 1

for test_case in range(1, T+1):
    size, select_honey, max_honey = map(int, input().split())
    honey_matrix = [list(map(int, input().split())) for _ in range(size)]
    my_max = 0
    my_max_2 = 0
    my_list = [0]*select_honey
    visited = [[0] * size for _ in range(size)]
    for column in range(len(honey_matrix)):
        for row in range(len(honey_matrix[column])):
            my_sum = 0
            if row + select_honey <= size:
                for idx in range(select_honey):
                    my_sum += honey_matrix[column][row+idx]
                    my_list[idx] = (honey_matrix[column][row+idx])**2
                if my_sum < max_honey:
                    if my_max < sum(my_list):
                        my_max = sum(my_list)
                        visited = [[0]*size for _ in range(size)]
                        for idx_2 in range(select_honey):
                            visited[column][row+idx_2] = 1

    # for column_2 in range(len(honey_matrix)):
    #     for row_2 in range(len(honey_matrix[column_2])):
    #         if not visited[column_2][row_2]:
    #             my_sum = 0
    #             if row_2 + select_honey <= size:
    #                 for idx_3 in range(select_honey):
    #                     my_sum += honey_matrix[column_2][row_2 + idx_3]
    #                     my_list[idx_3] = (honey_matrix[column_2][row_2 + idx_3]) ** 2
    #                 if my_sum < max_honey:
    #                     if my_max_2 < sum(my_list):
    #                         my_max_2 = sum(my_list)


