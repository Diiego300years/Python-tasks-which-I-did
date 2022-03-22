
def GiveWorkingDay(year, month, day):
    #prints the nearest working day date
    from datetime import date
    from datetime import timedelta

    #day = date.today() rezygnuje na potrzeby funkcji z daty dzisiejszej
    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day +timedelta(days=2)
        print(workingday)
    elif day.weekday() == 6:
        workingday = day +timedelta(days=1)
        print(workingday)
    else:
        workingday = day
        print(workingday)
    return workingday

nextworkingday = GiveWorkingDay(2022,9,1)
#print(nextworkingday)