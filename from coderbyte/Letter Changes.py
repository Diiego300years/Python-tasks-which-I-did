"""Have the function LetterChanges(str) take the str parameter being passed and modify it using the
following algorithm. Replace every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u)
and finally return this modified string.

Examples
Input: "hello*3"
Output: Ifmmp*3
Input: "fun times!"
Output: gvO Ujnft!"""

def LetterChanges(strParam):

  # code goes here
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  vowels = "aeiou"
  submite = ""
  ans = ""
  for i in strParam:
    if strParam == " ":
      submite += " "
    elif i.isalpha():
      submite += chr(ord(i) +1)
    else:
      submite += i

  for w in submite:
    if w in vowels:
      ans += w.upper()
    else:
      ans += w

  return ans

# keep this function call here
print(LetterChanges("hello*3"))