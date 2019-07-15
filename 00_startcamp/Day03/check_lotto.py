my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 7]
bonus = 6
# second = 0
# true = 0
# # my 와 real 의 6개가 같으면 1등
# # my 와 real 이 5개가 같고 나머지 하나가 bonus 면 2등
# # my 와 real 이 5개가 같으면 3등
# # '' 4개가 같으면 4등
# # '' 3개가 같으면 5등
# # 나머지는 꽝

# for i in range(6):
#     for j in range(6):
#         if my[i] == real[j]:
#             true = true + 1

# for k in range(6):
#     if my[k] == bonus:
#         second = 1

# if true == 6:
#     print('1등')
# elif (true == 5) and (second == 1):
#     print('2등')
# elif true == 5:
#     print('3등')
# elif true == 4:
#     print('4등')
# elif true == 3:
#     print('5등')
# else:
#     print('꽝')




# match_count = 0
# is_bonus = False

# for i in my:
#     if i == bonus:
#         is_bonus = True

#     for j in real:
#         if i == j:
#             match_count = match_count + 1  # match_count += 1
# if match_count == 6:
#     result = '1등'
# elif match_count == 5:
#     if is_bonus:
#         result = '2등'
#     else:
#         result = '3등'
# elif match_count == 4:
#     result = '4등'
# elif match_count == 3:
#     result = '5등'
# else:
#     result = '꽝'

# print(result)  # print는 디버깅용, 확인하는 용도 값은 저장해야함.


# match_count = 0

# for i in my:
#     for j in real:
#         if i == j:
#             match_count = match_count + 1  # match_count += 1
# if match_count == 6:
#     result = '1등'
# elif match_count == 5:
#     if bonus in my:
#         result = '2등'
#     else:
#         result = '3등'
# elif match_count == 4:
#     result = '4등'
# elif match_count == 3:
#     result = '5등'
# else:
#     result = '꽝'

# print(result)

match = set(my).intersection(set(real))
# 집합으로 만드는 합수, 순서가 없다.
# intersection 교집합
# [1, 2, 3] => list / {1, 2, 3} => set / (1, 2, 3) => tuple / {'a': 'A'} => dict
match_count = len(match)

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'

print(result)
