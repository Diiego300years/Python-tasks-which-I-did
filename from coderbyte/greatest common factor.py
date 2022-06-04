#greatest common factor from 2 positive digits

def GCF(arr):
    # code goes here
    count = 0

    if max(arr) % min(arr) == 0:
        return min(arr)

    for i in range(1, max(arr) + 1):
        if (max(arr) % i == 0) and (min(arr) % i == 0):
            count = i

    return count


# keep this function call here
print(GCF([45, 12]))