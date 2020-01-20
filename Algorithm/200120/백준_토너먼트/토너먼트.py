import sys

sys.stdin = open('input.txt')

people_count, kim, im = map(int, input().split())
tournament_list = [i+1 for i in range(people_count)]
flag = 1
count = 0
while flag:
    if not tournament_list:
        count = -1
        break
    result = []
    for i in range(len(tournament_list)//2):
        if (tournament_list[2*i] == kim and tournament_list[2*i+1] == im) or (tournament_list[2*i] == im and tournament_list[2*i+1] == kim):
            flag = 0
            break
        if tournament_list[2*i] == kim:
            result.append(kim)
        elif tournament_list[2*i+1] == kim:
            result.append(kim)
        elif tournament_list[2*i+1] == im:
            result.append(im)
        elif tournament_list[2*i+1] == im:
            result.append(im)
        else:
            result.append(tournament_list[2*i])
    if len(tournament_list)%2:
        result.append(tournament_list[-1])
    tournament_list = result[:]
    count += 1
print(count)