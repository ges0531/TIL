def road_solve(solved_road, count, visited, my_max, my_result):
    if count == 0 or sum(visited) == len(visited):
        result = 0
        for i in visited:
            if i == 1:
                result += 1
            else:
                my_max = max(result, my_max)
                result = 0
        my_result.append(max(result, my_max))
        return
    for j in range(len(solved_road)):
        if not visited[j]:
            visited[j] = 1
            if solved_road[j] == '0':
                road_solve(solved_road, count - 1, visited, my_max,  my_result)
                visited[j] = 0

def solution(road, n):
    my_result = []
    road_solve(road, n, [0]*len(road), 0, my_result)
    answer = max(my_result)
    return answer

solution('111011110011111011111100011111', 3)