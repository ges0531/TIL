import sys

sys.stdin = open('input.txt', 'r')


def comb(n, r, t, a, max_number):
    global my_num
    if r == 0:
        if (max_number-sum(t)) >= 0:
            if my_num > max_number-sum(t):
                my_num = max_number-sum(t)
    elif n < r:
        return
    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1, t, a, max_number)
        comb(n-1, r, t, a, max_number)

card_count, max_num = map(int, input().split())
player_num = list(map(int, input().split()))
my_num = 300000
comb(card_count, 3, [0]*3, player_num, max_num)
print(max_num - my_num)
