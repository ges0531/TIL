my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 6]
bonus = 7

# my 와 real 의 6개가 같으면 1등
# my 와 real 이 5개가 같고 나머지 하나가 bonus 면 2등
# my 와 real 이 5개가 같으면 3등
# '' 4개가 같으면 4등
# '' 3개가 같으면 5등
# 나머지는 꽝

for i in range(6):
    for j in range(6):
        if my[i] == real[j]:
            true = 1
            true = true + 1

if true == 6:
    print('1등')
elif true == 5:
    print('3등')
elif true == 4:
    print('4등')
elif true == 3:
    print('5등')
else:
    print('꽝')
