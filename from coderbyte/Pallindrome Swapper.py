
def PalindromeSwapper(strParam):

  # code goes here
  for i in range(len(strParam)-1):
    strList = list(strParam)
    strList[i],strList[i+1] = strList[i+1],strList[i]
    otherString = "".join(strList)
    if otherString == otherString[::-1]:
      return(otherString)
  return "-1"


# keep this function call here
print(PalindromeSwapper("rcaecar"))