def Weekday(dayNumber):

    names = {
        0: 'pon',
        1: 'wt',
        2: 'śr',
        3: 'czw',
        4: "pt",
        5: 'sb',
        6: 'nd'
    }
    return names.get(dayNumber, "error")

print(Weekday(6))