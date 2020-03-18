import datetime


def getDays(year, month):
    if month == 2:
        return (29 if ((year % 4) == 0) and ((year % 100) != 0) or ((year % 400 ) == 0) else 28)
    return date_dict[month]
    

dt = datetime.datetime.today()
date_dict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
print(getDays(dt.year, dt.month))
