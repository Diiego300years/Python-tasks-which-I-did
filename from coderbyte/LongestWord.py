#finding longest word without special characters

def LongestWord(sen):
    # code goes here
    sen2 = sen
    ans = ""
    arr = []
    new_sep = ' '
    seplist = [
        '!', '@', '#', '$', '%', '&', '*', '[', ']', '(', ')', ':',
        ',', '.', ';', '?', '/', '\\', '"', "'", '{', '}', '|', '?',
        '~', '^', 'Â´', '`',
    ]

    for sep in seplist:
        sen2 = sen2.replace(sep, new_sep)

    n = 0
    Split = sen2.split(" ")
    for i in Split:
        if len(i) > n:
            n = len(i)
            ans = i

    return ans


# keep this function call here
print(LongestWord("hello world"))