import unittest

"reachnge every divisible 3 by the word Fizz and every dvisible by 5 wit buz" \
"if digit culd be divisible with 3 and 5 return FizzBuzz"

#  3 reutrn Fizz
#5 return Buzz
#input 3:
# 1 2 fizz

#input 8
# 1 2 fizz 4 Buzz Fizz 7 8

def FizzBuzz(num):
    string = ""

    for i in range(1, num + 1):
        if i % 3 == 0:
            string += "fizz "
        if i % 5 == 0:
            string += "Buzz "
        if i % 3 == 0 and i % 5 == 0:
            string += "FizzBuzz "
        if i % 3 != 0 and i % 5 != 0:
            string += f"{str(i)} "



    return string

print(FizzBuzz(31))

