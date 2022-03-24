"""Napisać funkcję split(x), która podzieli zadaną liczbę x (przy x>6)
na dwie liczby całkowite a i b, przy czym liczba a ma być podzielna przez 3, a liczba b spełnia
3<b<=6.

Przykłady
split(7) = (3,4)
split(8) = (3,5)
split(11) = (6,5)
split(12) = (6,6)"""
# x = 7


def split(x: int):
    #this function should return 2 int one of them split by 3 and second could be anything
    a = 0
    b = 0
    if int(x) > 6:
        c = int(x) / 2
        if int(c) % 3 == 0:
            a += int(c)
            b = x - a
            #print(a, b)
        else:
            if int(c) % 3 != 0:
                b += int(c)
                a = x - int(c)
                #print(a, b)
    return a, b
print(split(7))