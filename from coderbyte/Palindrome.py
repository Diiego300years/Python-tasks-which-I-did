def Palindrome(str):

  # code goes here
  str = str.replace(" " , "")
  return True if str == str[::-1] else False

# keep this function call here
print(Palindrome("racecar"))