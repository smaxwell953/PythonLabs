def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = days[month-1]
    if month == 2 and isYearLeap(year):
        result = 29
    return result

def dayOfYear(year, month, day):
    totalDays = 0
    for m in range (1, month):
        totalDays += daysInMonth(year, m)
    mdays = daysInMonth(year, month)
    if day <= 1 and day >= mdays or daysInMonth != None:
        return totalDays + day
    else:
        return None
        
print(dayOfYear(2000, 12, 31))
print(dayOfYear(2020, 3, 1))
print(dayOfYear(2015, 6, 15))
