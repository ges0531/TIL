import sys

sys.stdin = open('input.txt', 'r')

queue_count, find_count = map(int, input().split())

queue_list = [i+1 for i in range(queue_count)]
find_list = list(map(int, input().split()))
count = 0
result_count_1 = 0
result_count_2 = 0
index = 0
count_2 = 0
while count != find_count:
    result_count_1 = 0
    result_count_2 = 0
    index_left = 0
    index_right = 0
    if queue_list[0] == find_list[index]:
        count += 1
        queue_list.pop(0)
        index += 1
    else:
        while queue_list[index_left] != find_list[index]:
            index_left += 1
            result_count_1 += 1
        while queue_list[index_right] != find_list[index]:
            index_right -= 1
            result_count_2 += 1
        if result_count_1 < result_count_2:
            while queue_list[0] != find_list[index]:
                queue_list.append(queue_list.pop(0))
            count_2 += result_count_1
        else:
            while queue_list[0] != find_list[index]:
                queue_list = [queue_list.pop(-1)] + queue_list
            count_2 += result_count_2
print(count_2)