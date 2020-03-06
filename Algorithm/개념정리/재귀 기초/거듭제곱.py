def power(x, y):
    # 코드를 작성하세요.
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y//2) * power(x, y//2)
    else:
        return x * power(x, y//2) * power(x, y//2)

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))