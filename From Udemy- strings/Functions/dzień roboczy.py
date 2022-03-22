"""def GiveWorkingDay():
    #prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    day = date.today()
    #day = date(2017,9,30)

    if day.weekday() == 5:
        workingday = day +timedelta(days=2)
        print(workingday)
    elif day.weekday() == 6:
        workingday = day +timedelta(days=1)
        print(workingday)
    else:
        workingday = day
        print(workingday)
    return print('working day for', day,'is',workingday)

print(GiveWorkingDay())"""

#function for parameters

def GiveWorkingDay(year, month, day):
    #prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    #day = date.today() rezygnuje na potrzeby funkcji z daty dzisiejszej
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day +timedelta(days=2)
        print(workingday)
    elif day.weekday() == 6:
        workingday = day +timedelta(days=1)
        print(workingday)
    else:
        workingday = day
        print(workingday)
    return print('working day for', day,'is',workingday)

print(GiveWorkingDay(2022,3,4))
print(GiveWorkingDay(day=5,month=3,year=2022))