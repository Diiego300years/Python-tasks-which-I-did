#My algoritm for star raiting

def StarRating(strParam):
    # code goes here
    s = strParam.split(".")

    strP = "0."
    strP += str(s[1])

    stars = [0, 1, 2, 3, 4]

    count_1 = 0
    count_2 = 0

    if float(strParam) == 5:
        return ("full ") * 5

    for i in range(len(stars) - 1):
        if int(stars[i]) < int(s[0]):
            count_1 += 1
        if int(stars[i]) < float(strP):
            if float(strP) > 0.25:
                count_2 += 1
            if float(strP) >= 0.75:
                count_1 += 1
                count_2 -= 1

    ans_full = "full "
    ans_half = "half "

    digit = 0

    if len(count_1 * ans_full + ans_half * count_2) != 25:
        digit = (25 - len(count_1 * ans_full + ans_half * count_2)) / 5

    em = "empty "

    return count_1 * ans_full + ans_half * count_2 + em * int(digit)


# keep this function call here
print(StarRating("3.75"))