"""Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'"""


#bo to jest pętla i cały czas sie od poczatku wykonuje i zapętla przez to jest taki wynik a nie inny....
#zapętla się i dodaje ciągle od poczatku tu o to chodziło to co od poczatku plus następne, a dodajemy
# 1 zeby się wykonala do końca

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    print(str[:i + 1])
    result = result + str[:i+1]
  return result

print(string_splosion("Code"))

num = [2,3,9,5,6]
for i in range(len(num)):
  print(num[i])