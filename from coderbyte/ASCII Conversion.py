#should return dec there
def ASCIIConversion(strParam):
  result = ""
  # code goes here
  for i in strParam:
    if i == ' ':
      result += ' '
    else:
      result += str(ord(i))

  return result

# keep this function call here
print(ASCIIConversion("Hello there"))

