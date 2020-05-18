def solution(numbers, hand):
    answer = []
    left_location = [3, 0]
    right_location = [3, 2]
    phone_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}
    for j in numbers:
        if j in [1, 4, 7]:
            answer.append('L')
            left_location = phone_dict[j]
        elif j in [3, 6, 9]:
            answer.append('R')
            right_location = phone_dict[j]
        else:
            if cal(left_location, phone_dict[j]) < cal(right_location, phone_dict[j]):
                answer.append('L')
                left_location = phone_dict[j]
            elif cal(left_location, phone_dict[j]) > cal(right_location, phone_dict[j]):
                answer.append('R')
                right_location = phone_dict[j]
            else:
                if hand == 'left':
                    answer.append('L')
                    left_location = phone_dict[j]
                else:
                    answer.append('R')
                    right_location = phone_dict[j]
    answer = ''.join(answer)
    return answer



def cal(start_node, end_node):
    result = abs(start_node[0] - end_node[0]) + abs(start_node[1] - end_node[1])
    return result

# def BFS(start_node, end_node):
#     queue = [start_node]
#     visited = [[0] * 3 for _ in range(4)]
#     visited[start_node[0]][start_node[1]] = 1
#     dy = [-1, 1, 0, 0]
#     dx = [0, 0, -1, 1]
#     result = 0
#     while queue:
#         a = queue.pop()
#         y = a[0]
#         x = a[1]
#         if a == end_node:
#             result = visited[y][x]-1
#             break
#         for i in range(4):
#             idy = y + dy[i]
#             idx = x + dx[i]
#             if 0 <= idy < 4 and 0 <= idx < 3:
#                 if not visited[idy][idx]:
#                     visited[idy][idx] = visited[y][x] + 1
#                     queue.append([idy, idx])
#     return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))