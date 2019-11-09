def solution(board, moves):
    my_list = [0]
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1]:
                if my_list[-1] == board[j][moves[i]-1]:
                    my_list.pop()
                    answer += 1
                else:
                    my_list.append(board[j][moves[i]-1])
                board[j][moves[i] - 1] = 0
                break
    return answer*2


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))