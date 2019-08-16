num = 456789  # Baby Gin 확인할 6자리 수
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
num = list(num)
for number in num:
    if num.count(number) == 6:
        return 'Baby_Gin'
    elif num.count(number) == 3:
        for i in range(3):
            num.pop(num.index(i))