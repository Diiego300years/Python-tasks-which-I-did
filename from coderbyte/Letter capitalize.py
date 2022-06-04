def LetterCapitalize(text):
    words = text.split(' ')
    newWords = []
    for word in words:
        newWords.append(word[0].upper() + word[1:])
    return ' '.join(newWords)


# keep this function call here
print(LetterCapitalize("hello world"))