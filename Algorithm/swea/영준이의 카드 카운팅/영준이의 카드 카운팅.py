import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    card = list(input())
    cards = [0] * (len(card)//3)
    S_count = D_count = H_count = C_count = 13
    a = 0
    for i in range(len(card)//3):
        cards[i] = card[3*i]+card[3*i+1]+card[3*i+2]
    for j in cards:
        if cards.count(j) >= 2:
            a = 1
        else:
            if 'S' in j:
                S_count -= 1
            elif 'D' in j:
                D_count -= 1
            elif 'H' in j:
                H_count -= 1
            elif 'C' in j:
                C_count -= 1
    if a == 0:
        print('#{} {} {} {} {}'.format(test_case, S_count, D_count, H_count, C_count))
    else:
        print('#{} ERROR'.format(test_case))