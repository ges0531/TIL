def solution(N, coffee_times):
    answer = []
    flag = 0
    while coffee_times:
        if len(coffee_times) < N:
            N = len(coffee_times)
        for i in range(N):
            coffee_times[i] -= 1
            if coffee_times[i] == 0:
                flag += 1
                answer.append(i + flag)
        for j in range(N - 1, -1, -1):
            if coffee_times[j] == 0:
                coffee_times.pop(j)

    return answer

print(solution(3, [4, 2, 2, 5, 3]))