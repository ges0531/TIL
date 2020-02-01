import sys

sys.stdin = open('input.txt', 'r')

classroom_count = int(input())
student_count = list(map(int, input().split()))
first_director, second_director = map(int, input().split())
result = 0
for i in range(classroom_count):
    student_count[i] -= first_director
    if student_count[i] > 0:
        if student_count[i] % second_director:
            result += ((student_count[i] // second_director)+1)
        else:
            result += (student_count[i] // second_director)
    result += 1
print(result+classroom_count)
