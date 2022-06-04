#checking is digit even

def SimpleEvens(num):
    # code goes here

    for i in str(num):
        if int(i) % 2 != 0:
            return False

    return True


# keep this function call here
print(SimpleEvens(input()))