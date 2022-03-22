def FirstFactorial(num: int):

  # code goes here
  factorial = 1
  for i in range (1, num + 1):
    factorial *= i

  return factorial
# keep this function call here

ip = input()
print(FirstFactorial(int(ip)))