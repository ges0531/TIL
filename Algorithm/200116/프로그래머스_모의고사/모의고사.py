def solution(answers):
    one_math = [1, 2, 3, 4, 5]
    two_math = [2, 1, 2, 3, 2, 4, 2, 5]
    three_math = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    math_exam = [one_math, two_math, three_math]
    answer = []


    def solve_func(math_list, student_index, math_index, count):
        if math_index >= len(answers):
            answer.append(count)
            return
        if student_index < len(math_list):
            if math_list[student_index] == answers[math_index]:
                solve_func(math_list, student_index+1, math_index+1, count+1)
            else:
                solve_func(math_list, student_index + 1, math_index + 1, count)
        else:
            solve_func(math_list, 0, math_index, count)
    for i in range(len(math_exam)):
        solve_func(math_exam[i], 0, 0, 0)
    max_number = max(answer)
    for j in range(len(answer)-1, -1, -1):
        if max_number == answer[j]:
            answer[j] = j+1
        else:
            answer.pop(j)
    return sorted(answer)
my_list = []
for jj in range(10000):
    my_list += [1]

print(solution(my_list))