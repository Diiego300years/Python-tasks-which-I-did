def missing_char(str, n):
    #this function delete a word wchich You would like
  for i in range(len(str)):
    if n == i:
      return str.replace(str[i],"")

for i in range(0, 23):
    print(i)