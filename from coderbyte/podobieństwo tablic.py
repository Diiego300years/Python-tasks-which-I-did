def FindIntersection(strArr):
    # code goes here

    empty_1 = ''
    empty_2 = ''
    table = []

    for i in strArr[0]:
        empty_1 += i
        # print(b)
    for ii in strArr[1]:
        empty_2 += ii

    # SECOND PART OF JOB

    full_1 = empty_1.split(",")
    full_2 = empty_2.split(",")

    for i in full_1:
        for ii in full_2:
            if i == ii:
                table.append(i)

    # Resaults
    result_1 = ''

    for i in table:
        result_1 += i

    return result_1.replace(' ', ',')


# keep this function call here
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))