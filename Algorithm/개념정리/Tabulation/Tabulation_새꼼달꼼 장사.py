def max_profit(price_list, count):
    table = {0: 0, 1: price_list[1]}
    for i in range(2, count+1):
        if i < len(price_list):
            table[i] = price_list[i]
        else:
            table[i] = 0
        for j in range(i//2+1):
            if table[i-j] + table[j] > table[i]:
                table[i] = table[i-j] + table[j]
    return table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
