#chcecking if x's is equal to o's

def ExOh(str):

  # code goes here
  count_x = 0
  count_o = 0

  for i in range(len(str)):
    count_x +=1 if str[i] == "x" else False
    count_o +=1 if str[i] == "o" else False

  return count_x == count_o


# keep this function call here
print(ExOh("xxooxo"))