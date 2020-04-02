import sys

sys.stdin = open('input.txt', 'r')

people_count = int(input())
big_people = [list(map(int, input().split())) for _ in range(people_count)]
rank_list = [0]*people_count
for i in range(people_count):
    my_count_1 = 1
    for j in range(people_count):
        if i != j:
            if big_people[i][0] < big_people[j][0] and big_people[i][1] < big_people[j][1]:
                my_count_1 += 1
    rank_list[i] = my_count_1
print(' '.join(map(str, rank_list)))