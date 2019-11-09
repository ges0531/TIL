def solution(k, room_number):
    visited = [0]*(k+1)
    answer = []
    for i in range(len(room_number)):
        if not visited[room_number[i]]:
            visited[room_number[i]] = 1
            answer.append(room_number[i])
        else:
            a = room_number[i]
            flag = 1
            while flag:
                a += 1
                if not visited[a]:
                    visited[a] = 1
                    answer.append(a)
                    flag = 0
    return answer


k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))