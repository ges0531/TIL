import sys
import itertools

sys.stdin = open('input.txt', 'r')


while True:
    number_list = list(map(int, input().split()))
    if number_list[0] == 0:
        break
    my_list = []
    for i in itertools.combinations(number_list, 6):
        if len(set(i)) == 6 and sorted(i) not in my_list:
            my_list.append(sorted(i))
    my_list.sort()
    for j in my_list:
        j = map(str, j)
        print(' '.join(j))
    print()
