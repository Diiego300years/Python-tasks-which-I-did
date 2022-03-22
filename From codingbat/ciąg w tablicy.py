
"""Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True"""

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

# musi być tak bo nie może iść pętla bo tablicy i + 1 bo przecież tablica się kończy co nie xdd a może być do 3 znaków
#czyli 0, 1, 2 dlatego niech się wykonuje do range(len(nums)-2)