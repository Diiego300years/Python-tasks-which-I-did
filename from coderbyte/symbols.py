
def SimpleSymbols(str):
    # code goes here
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if len(str) < 3:
        return 'false'

    if (str[0] in letters) or (str[-1] in letters):
        return 'false'

    for i in range(1, len(str) - 1):
        if str[i] in letters:
            if not (str[i - 1] == '+' and str[i + 1] == '+'):
                return 'false'

    return 'true'