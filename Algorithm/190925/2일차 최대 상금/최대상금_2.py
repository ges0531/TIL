import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    game_count = list(input().split())
    real_game_num = list(game_count.pop(0))
    game_count[0] = int(game_count[0])
    index = []
    for k in range(len(real_game_num)):
        if real_game_num.count(real_game_num[k]) >= 3:
            index.append(k)
    real_game_num_2 = sorted(real_game_num)

    my_max = 0
    count = 0
    for ii in range(game_count[0]):
        for i in range(len(real_game_num)):
            for j in range(i, len(real_game_num)):
                origin_num = ''.join(real_game_num)
                if real_game_num.count(real_game_num[j]) >= 3 and real_game_num[i] == real_game_num_2[0]:
                    real_game_num[i], real_game_num[index[-1]] = real_game_num[index[-1]], real_game_num[i]
                    change_num = ''.join(real_game_num)
                    real_game_num[i], real_game_num[index[-1]] = real_game_num[index[-1]], real_game_num[i]
                elif real_game_num.count(real_game_num[j]) >= 3 and real_game_num[i] == real_game_num_2[1]:
                    real_game_num[i], real_game_num[index[-2]] = real_game_num[index[-2]], real_game_num[i]
                    change_num = ''.join(real_game_num)
                    real_game_num[i], real_game_num[index[-2]] = real_game_num[index[-2]], real_game_num[i]
                else:
                    real_game_num[i], real_game_num[j] = real_game_num[j], real_game_num[i]
                    change_num = ''.join(real_game_num)
                    real_game_num[i], real_game_num[j] = real_game_num[j], real_game_num[i]
                if int(origin_num) > int(change_num):
                    if my_max < int(origin_num):
                        my_max = int(origin_num)
                else:
                    if my_max < int(change_num):
                        my_max = int(change_num)
        if real_game_num == list(str(my_max)):
            count += 1
        else:
            real_game_num = list(str(my_max))
    my_max = list(str(my_max))
    if count != 0 and (game_count[0]-count)%2:
        my_max[-1], my_max[-2] = my_max[-2], my_max[-1]
    print('#{} {}'.format(test_case, ''.join(my_max)))