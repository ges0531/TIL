def comb(n, r, arr):
    global a
    if r == 0:
        if tr[0] == tr[1] == tr[2]:
            a = 1
            return
        elif ((min(tr)+1) in tr) and ((min(tr)+2) in tr):
            a = 1
            return
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        comb(n-1, r-1, arr)
        comb(n-1, r, arr)


T = int(input())

for test_case in range(1, T+1):
    card_list = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    for ii in range(12):
        if ii % 2:
            player_2.append(card_list[ii])
        else:
            player_1.append(card_list[ii])
    player_game_1 = []
    player_game_2 = []
    b = 0
    for j in range(6):
        a = 0
        player_game_1.append(player_1.pop(0))
        player_game_2.append(player_2.pop(0))
        tr = [0]*3
        if len(player_game_1) >= 3:
            comb(len(player_game_1), 3, player_game_1)
            if a == 1:
                b = 1
                print('#{} {}'.format(test_case, 1))
                break
            else:
                comb(len(player_game_2), 3, player_game_2)
                if a == 1:
                    b = 1
                    print('#{} {}'.format(test_case, 2))
                    break
    if b == 0:
        print('#{} {}'.format(test_case, 0))