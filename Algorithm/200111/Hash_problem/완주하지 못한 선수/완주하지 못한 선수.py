def solution(participant, completion):
    visited = [0]*len(completion)
    for par in participant:
        for comp in range(len(completion)):
            if not visited[comp]:
                if par == completion[comp]:
                    visited[comp] = 1
                    break
        else:
            answer = par
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))