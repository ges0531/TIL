def solution(progresses, speeds):
    answer = []
    while progresses:
        for dev_time in range(len(progresses)):
            if progresses[dev_time] < 100:
                progresses[dev_time] += speeds[dev_time]
        if progresses[0] >= 100:
            count = 0
            while progresses:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    count += 1
                else:
                    break
            answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
