def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    coin_list.sort()
    flag = len(coin_list)-1
    count = 0
    while flag >= 0:
        if value-coin_list[flag] >= 0:
            value -= coin_list[flag]
            count += 1
        else:
            flag -= 1
    return count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))