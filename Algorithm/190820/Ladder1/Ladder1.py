import sys


sys.stdin = open('input.txt', 'r')


T = 10

for test_case in range(1, T+1):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    ladder = []
    case_num = int(input())
    for _ in range(1, 101):
        matrix = list(map(int, input().split()))
        ladder.append(matrix)

    count = 99
    for i in ladder[count]:
        if i == 2:
            location = [count, ladder[count].index(i)]
    while count >= 0:
        if location[1] - 1 >= 0 and location[1] + 1 <= 99:
            if ladder[count][location[1] - 1] == 0 and ladder[count][location[1] + 1] == 0:
                count -= 1
            elif ladder[count][location[1] - 1] == 1 and ladder[count][location[1] + 1] == 0:
                ladder[count][location[1]] = 0
                location[1] -= 1
            elif ladder[count][location[1] - 1] == 0 and ladder[count][location[1] + 1] == 1:
                ladder[count][location[1]] = 0
                location[1] += 1
        elif location[1] + 1 <= 99:
            if ladder[count][location[1] + 1] == 0:
                count -= 1
            else:
                ladder[count][location[1]] = 0
                location[1] += 1
        elif location[1] - 1 >= 0:
            if ladder[count][location[1] - 1] == 0:
                count -= 1
            else:
                ladder[count][location[1]] = 0
                location[1] -= 1
        location = [count, location[1]]
    print('#{} {}'.format(test_case, location[1]))


    # count = 99
    # for i in ladder[count]:
    #     if i == 2:
    #         location = (count, ladder[count].index(i))
    #         print(test_case)
    # while count >= 0:
    #     location = (count, location[1])
    #     if location[1] + dy[0] >= 0 and location[1] + dy[1] <= 99:
    #         if ladder[count][location[1] + dy[0]] == 0 and ladder[count][location[1] + dy[1]] == 0:
    #             print(location, 2)
    #             count -= 1
    #         elif ladder[count][location[1] + dy[0]] == 1 and ladder[count][location[1] + dy[1]] == 0:
    #             print(location, 3)
    #             while ladder[count][location[1] + dy[0]] == 1:
    #                 location = (count, location[1] + dy[0])
    #                 if location[1] == 0:
    #                     break
    #             count -= 1
    #         elif ladder[count][location[1] + dy[0]] == 0 and ladder[count][location[1] + dy[1]] == 1:
    #             print(location, 4)
    #             while ladder[count][location[1] + dy[1]] == 1:
    #                 location = (count, location[1] + dy[1])
    #             count -= 1
    #     elif location[1] + dy[1] <= 99:
    #         if ladder[count][location[1] + dy[1]] == 0:
    #             print(location, 2)
    #             count -= 1
    #         elif ladder[count][location[1] + dy[1]] == 1:
    #             print(location, 4)
    #             while ladder[count][location[1] + dy[1]] == 1:
    #                 location = (count, location[1] + dy[1])
    #     elif location[1] + dy[0] >= 0:
    #         if ladder[count][location[1] + dy[0]] == 0:
    #             print(location, 2)
    #             count -= 1
    #         elif ladder[count][location[1] + dy[0]] == 1:
    #             print(location, 3)
    #             while ladder[count][location[1] + dy[0]] == 1:
    #                 location = (count, location[1] + dy[0])
    #     print(location)

