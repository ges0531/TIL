def solution(inputString):
    bracket_dict = {'(': 0, '{': 0, '[': 0, '<': 0}
    answer = 0
    for i in inputString:
        if i == '(':
            bracket_dict['('] += 1
        elif i == ')':
            if bracket_dict['(']:
                bracket_dict['('] -= 1
                answer += 1
        elif i == '{':
            bracket_dict['{'] += 1
        elif i == '}':
            if bracket_dict['{']:
                bracket_dict['{'] -= 1
                answer += 1
        elif i == '[':
            bracket_dict['['] += 1
        elif i == ']':
            if bracket_dict['[']:
                bracket_dict['['] -= 1
                answer += 1
        elif i == '<':
            bracket_dict['<'] += 1
        elif i == '>':
            if bracket_dict['<']:
                bracket_dict['<'] -= 1
                answer += 1
    for j in bracket_dict:
        if bracket_dict[j] != 0:
            answer -= 1
            break
    return answer

print(solution('if (Count of eggs is 4.) {Buy milk.}'))