T = int(input())

for test_case in range(1, T+1):
    container_count, truck_count = map(int, input().split())
    container_weight = sorted(list(map(int, input().split())), reverse=True)
    truck_stack = sorted(list(map(int, input().split())), reverse=True)
    my_sum = 0
    index = 0
    for i in range(len(container_weight)):
        if container_weight[i] <= truck_stack[index]:
            my_sum += container_weight[i]
            index += 1
        if index == len(truck_stack):
                break
    print('#{} {}'.format(test_case, my_sum))