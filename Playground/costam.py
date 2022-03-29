print(7-8)

def get_hig_num(numbers: list) -> tuple:
    the_h_n = max(numbers)
    index = numbers.index(the_h_n)
    return (the_h_n, index)

print(get_hig_num([5,6,8,1,2,4]))


w = [2,5,9,11]

for i in w:
    i *= 2
w.append('crash')



print(w)

print(9%2)

for i in range(5):
    print(i, i*2)

print(10%3)
