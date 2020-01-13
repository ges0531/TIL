def solution(progresses, speeds):
    answer = []
    visited = [0]*len(progresses)
    flag = 1
    while flag:
        for dev_time in range(len(progresses)):
            if progresses[dev_time] < 100:
                progresses[dev_time] += speeds[dev_time]
                visited[dev_time] += 1
                flag = 1
            else:
                flag = 0
    a = visited[0]
    answer_count = 0
    while visited:
        if a >= visited[0]:
            answer_count += 1
            visited.pop(0)
        else:
            answer.append(answer_count)
            answer_count = 0
            a = visited[0]
    answer.append(answer_count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
