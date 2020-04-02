def solution(heights):
    answer = [0]*len(heights)
    for send_top in range(len(heights)-1, -1, -1):
        for reception_top in range(send_top-1, -1, -1):
            if heights[send_top] < heights[reception_top]:
                answer[send_top] = reception_top+1
                break
    return answer


print(solution([3, 9, 9, 3, 5, 7, 2]))
