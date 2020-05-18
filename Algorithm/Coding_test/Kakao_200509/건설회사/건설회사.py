def solution(board):
    global ans
    size = len(board)
    ans = 1000000000
    search_road([0, 0], [size-1, size-1], board, [[0]*size for _ in range(size)], 0, 4, [[0]*size for _ in range(size)])
    answer = ans-500
    return answer


def search_road(start_node, end_node, matrix, visited, result, direction, memoization):
    global ans
    if memoization[start_node[0]][start_node[1]] == 0:
        memoization[start_node[0]][start_node[1]] = result
    else:
        if result > memoization[start_node[0]][start_node[1]]:
            return
        else:
            memoization[start_node[0]][start_node[1]] = result
    if start_node == end_node:
        ans = min(ans, result)
        return
    y = start_node[0]
    x = start_node[1]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        idy = y + dy[i]
        idx = x + dx[i]
        if 0 <= idy < len(matrix) and 0 <= idx < len(matrix):
            if not visited[idy][idx]:
                if not matrix[idy][idx]:
                    visited[idy][idx] = 1
                    if direction == i:
                        search_road([idy, idx], end_node, matrix, visited, result+100, i, memoization)
                    else:
                        search_road([idy, idx], end_node, matrix, visited, result + 600, i, memoization)
                    visited[idy][idx] = 0
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
