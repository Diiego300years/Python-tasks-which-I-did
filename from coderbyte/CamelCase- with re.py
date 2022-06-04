import re

def CamelCase(str):

  # code goes here
  words = re.split(r'[^a-zA-Z]', str.lower())
  ans = words[0] +"".join(word.capitalize() for word in words[1:])
  return ans

# keep this function call here 
print(CamelCase("BOB loves-coding"))