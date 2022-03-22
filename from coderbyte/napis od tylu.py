def FirstReverse(strParam):
    # code goes here
    strLenght = len(strParam)
    slicedString = strParam[strLenght::-1]  # slicing

    return slicedString


# keep this function call here
print(FirstReverse(input()))
