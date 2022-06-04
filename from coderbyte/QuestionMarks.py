#it should be 10 equel of 2 numbers and 3 question marks between
def QuestionsMarks(str):
    # code goes here
    arr = []
    arr_2 = []

    for i in str:
        if i.isdigit() or i == "?":
            arr.append(i)

    count = 0
    count_2 = 0

    for i in arr:
        if i.isdigit():
            count += int(i)
            print(count, count_2)
        if i == "?":
            count_2 += 1
        if count == 10 and count_2 >= 3:
            return True

    return False


# keep this function call here
print(QuestionsMarks("arrb6???4xxbl5???eee5"))
#should return True