import sys

sys.stdin = open('input.txt', 'r')

people_count, drop_people = map(int, input().split())
people_list = [i+1 for i in range(people_count)]
index = 0
my_list= []
while people_list:
    index += (drop_people-1)
    while index >= people_count:
        index -= people_count
    my_list.append(people_list.pop(index))
    people_count -= 1
print('<', end='')
print(', '.join(map(str, my_list)), end='')
print('>')