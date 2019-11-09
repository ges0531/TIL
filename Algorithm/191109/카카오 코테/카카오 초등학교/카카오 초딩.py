def solution(stones, k):
    answer = 0
    count = 0
    while count < k:
        count = 0
        for i in range(len(stones)):
            stones[i] -= 1
            if stones[i] <= 0:
                count += 1
                if count == k:
                    break
            else:
                count = 0
        answer += 1
    return answer


stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
print(solution(stones, k))