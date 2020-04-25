def solution(purchase):
    price_list = []
    day_list = []
    month_list = []
    date = [1, 0]
    flag = 0
    result = 0
    validity_list = [0]*len(purchase)
    grade_list = [0]*5
    for i in range(len(purchase)):
        price = list(purchase[i].split(' '))
        price_list.append(int(price.pop()))
        date_split = price[0].split('/')
        day_list.append(int(date_split.pop()))
        month_list.append(int(date_split.pop()))
    month_list += [0]
    day_list += [0]
    for i in range(365):
        date[1] += 1
        if date[0] == month_list[flag] and date[1] == day_list[flag]:
            result += price_list[flag]
            validity_list[flag] = 31
            flag += 1
        for j in range(len(validity_list)):
            if validity_list[j]:
                validity_list[j] -= 1
                if validity_list[j] == 0:
                    result -= price_list[j]
        if date[1] == 31 and (date[0] in [1, 3, 5, 7, 8, 10, 12]):
            date[1] = 0
            date[0] += 1
        elif date[1] == 30 and (date[0] in [4, 6, 9, 11]):
            date[1] = 0
            date[0] += 1
        elif date[1] == 28 and date[0] == 2:
            date[1] = 0
            date[0] += 1
        if 0 <= result < 10000:
            grade_list[0] += 1
        elif 10000 <= result < 20000:
            grade_list[1] += 1
        elif 20000 <= result < 50000:
            grade_list[2] += 1
        elif 50000 <= result < 100000:
            grade_list[3] += 1
        elif 100000 <= result:
            grade_list[4] += 1

    answer = grade_list
    return answer

solution(["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"])