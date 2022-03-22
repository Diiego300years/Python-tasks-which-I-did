def LongestWord(sen):

  # code goes here
  max = 0
  splited = sen.split()
  for word in splited:
    if (len(word) > max and word.isalpha() and len(word) != max):   #isalpha() czy składa się tylko z liter
      max = len(word)
      largest = word
  return largest

# keep this function call here
print(LongestWord(input()))