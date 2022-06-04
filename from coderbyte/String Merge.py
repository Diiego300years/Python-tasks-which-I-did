#should return merge 2 strings
def StringMerge(strParam):
  # code goes here
  str = strParam.split("*")
  str_1 = str[0]
  str_2 = str[1]

  ans = ""

  for i, j in zip(str_1, str_2):
    ans += i
    ans += j

  return ans


# keep this function call here
print(StringMerge("123hg*aaabb"))