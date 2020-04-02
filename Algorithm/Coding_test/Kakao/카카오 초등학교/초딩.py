def solution(stones, k):
    count = 0
    answer = 0
    while count < k:
        for i in range(len(stones)):
            if stones[i]:
                stones[i] -= 1
        for j in range(len(stones)):
            if stones[j:j+k] == [0]*k:
                break
        answer += 1
    return answer


stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
print(solution(stones, k))