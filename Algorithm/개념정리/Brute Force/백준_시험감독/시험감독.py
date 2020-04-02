import sys

sys.stdin = open('input.txt', 'r')

classroom_count = int(input())
student_count = list(map(int, input().split()))
first_director, second_director = map(int, input().split())
first_list = [1]*classroom_count
end_flag = classroom_count
result = 0
while end_flag:
    for i in range(len(student_count)):
        if student_count[i]:
            if first_list[i]:
                if student_count[i] > first_director:
                    student_count[i] -= first_director
                    result += 1
                else:
                    student_count[i] = 0
                    end_flag -= 1
                first_list[i] -= 1
            else:
                if student_count[i] > second_director:
                    student_count[i] -= second_director
                    result += 1
                else:
                    student_count[i] = 0
                    end_flag -= 1
print(result+classroom_count)
