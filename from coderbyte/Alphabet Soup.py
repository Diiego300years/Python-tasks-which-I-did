
def AlphabetSoup(str):
    # code goes here
    ans = []
    submite = ""

    for i in range(len(str)):
        ans.append(str[i])

    for i in sorted(ans):
        submite += i

    return submite


# keep this function call here
print(AlphabetSoup("coderbyte"))