
#It should count vowels. I try comprehension from now
def VowelCount(str):
    # code goes here
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for i in str:
        count += 1 if i in vowels else False

    return count


# keep this function call here
print(VowelCount("adrianna"))