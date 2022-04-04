print("kanpka")

tab = "kanapka"
for i in range(len(tab)-1):
    print(tab[i])

if __name__ == '__main__':
    print("kanpka")

print(len("KA"))
a = [1,2]
print(len(a))
print(a[1])
diff = []
a = (1,2,3,4)
for x, y in zip(a[0::], a[1::]):
    diff.append(y - x)

print(diff)