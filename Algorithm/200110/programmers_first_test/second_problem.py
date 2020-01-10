def solution(x):
    my_sum = 0
    x = str(x)
    result = list(x)
    for i in result:
        my_sum += int(i)
    if int(x) % my_sum:
        answer = False
    else:
        answer = True
    return answer