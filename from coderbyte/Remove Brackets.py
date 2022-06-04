#should return how many brckets is more than we want

def RemoveBrackets(strParam):
    # code goes here
    rep = '()'
    while rep in strParam:
        strParam = strParam.replace(rep, '')

    return len(strParam)


# keep this function call here
print(RemoveBrackets("(()()(()"))