def solution(bridge_length, weight, truck_weights):
    run_truck = []
    visited = []
    answer = 0
    while truck_weights or run_truck:
        for truck_time in range(len(visited)):
            visited[truck_time] += 1
        if visited and visited[0] >= bridge_length:
            visited.pop(0)
            run_truck.pop(0)
        if truck_weights and (truck_weights[0] + sum(run_truck)) <= weight:
            run_truck.append(truck_weights.pop(0))
            visited.append(0)
        answer += 1
    return answer

print(solution(2, 10, [7, 4, 5, 6]))

